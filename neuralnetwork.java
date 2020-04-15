//*******************************************************************************************************************
// Name: John Wolz
// CWID: 102-51-920
// Date: October 16th, 2019
// Program #1: MNIST Handwritten Digit Recognizer Neural Network in Java
// Description: This program can train and test a neural network on recognizing
// handwritten digits (0-9) from the MNIST digit set.
//*******************************************************************************************************************

import java.io.*;
import java.util.*;

class NeuralNetwork
{
	static int input_size;
	static int[][] label;
	static double[][] value;

	static int minibatch_size;
	static int num_of_minibatches;
	static int[][] minibatch_labels;
	static double[][] minibatch_values;
	
	static int num_nodes_in_layer_input;
	static int num_nodes_in_layer_hidden;
	static int num_nodes_in_layer_output;
	static double[][] weights_01;
	static double[][] weights_12;
	static double[] biases_1;
	static double[] biases_2;
	static double[] a1;
	static double[] a2;
	static double[] d1;
	static double[] d2;
	static double[] bias_gradients_1;
	static double[] bias_gradients_2;
	static double[] total_bias_gradients_1;
	static double[] total_bias_gradients_2;
	static double[][] weight_gradients_01;
	static double[][] weight_gradients_12;
	static double[][] total_weight_gradients_01;
	static double[][] total_weight_gradients_12;
	
	static double z;
	static int[] total_outputs;
	static int[] correct_outputs;
	static double eta;
	static double cost;
	static List<Integer> indices;
	
	static PrintStream o;
	static PrintStream console;
	
	static void ReadInputFile(boolean testing) throws IOException
	{
		String file;
		
		if (testing)
		{
			file = "src\\mnist_test.csv";
		}
		else
		{
			file = "src\\mnist_train.csv";
		}
		
		@SuppressWarnings("resource")
		BufferedReader csvReader = new BufferedReader(new FileReader(file)); // reads file
		
		String row;
		int row_num = 0;
		
		while ((row = csvReader.readLine()) != null) // loops through rows of data, each row is 1 input
		{
			String[] data = row.split(",");
			
			label[row_num][Integer.valueOf(data[0])] = 1; // converts label to "1 hot" vector
			total_outputs[Integer.valueOf(data[0])]++; // counts how many of each label there are 
			
			for (int i = 1; i < 784; i++) // loops through all pixel values of the current row
			{
				value[row_num][i-1] = Double.valueOf(data[i]) / 255.0; // normalizes each pixel value and assigns it 
			}
			
			row_num ++;
			
		}
	}
	
	static void GenerateRandomWeightsAndBiases()
	{
		Random r = new Random();
		
		// randomizes weights between layer 0 and 1
		for (int i = 0; i < num_nodes_in_layer_hidden; i++)
		{
			for (int j = 0; j < 784; j++)
			{
				weights_01[i][j] = (r.nextDouble() * 2) - 1; // generates random value between -1 and 1 
			}
		}
		
		// randomizes weights between layer 1 and 2
		for (int i = 0; i < num_nodes_in_layer_output; i++)
		{
			for (int j = 0; j < num_nodes_in_layer_hidden; j++)
			{
				weights_12[i][j] = (r.nextDouble() * 2) - 1; // generates random value between -1 and 1
			}
		}
		
		// randomizes biases in first (hidden) layer
		for (int i = 0; i < num_nodes_in_layer_hidden; i++)
		{
			biases_1[i] = (r.nextDouble() * 2) - 1; // generates random value between -1 and 1
		}
		
		// randomizes biases in second (output) layer
		for (int i = 0; i < num_nodes_in_layer_output; i++)
		{
			biases_2[i] = (r.nextDouble() * 2) - 1; // generates random value between -1 and 1
		}
		
	}
	
	static void DetermineMinibatch(int minibatch_num)
	{		
		int minibatch_starting_index = minibatch_num * minibatch_size; // determines starting index based on what current minibatch
		Integer[] ind_arr = indices.toArray(new Integer[0]);
		
		for (int i = 0; i < minibatch_size; i++)
		{
			minibatch_labels[i] = label[ind_arr[minibatch_starting_index + i]];
			minibatch_values[i] = value[ind_arr[minibatch_starting_index + i]];
		}
	}
	
	static void WipeGradients()
	{
		// resets bias gradients of hidden layer and weight gradients between layer 0 and 1
		for (int i = 0; i < num_nodes_in_layer_hidden; i ++)
		{
			total_bias_gradients_1[i] = 0;
			
			for (int j = 0; j < num_nodes_in_layer_input; j++)
			{
				total_weight_gradients_01[i][j] = 0;
			}
		}
		
		// resets bias gradients of output layer and weight gradients between layer 1 and 2
		for (int i = 0; i < num_nodes_in_layer_output; i ++)
		{
			total_bias_gradients_2[i] = 0;
			
			for (int j = 0; j < num_nodes_in_layer_hidden; j++)
			{
				total_weight_gradients_12[i][j] = 0;
			}
		}
	}
	
	static void ForwardPass(double[] a0, int[] y)
	{
		double[] b; // bias
		//double z; // output before applying sigmoid function
		a1 = new double[num_nodes_in_layer_hidden];
		a2 = new double[num_nodes_in_layer_output];
		
		/// Layer 0 to 1
		for (int i = 0; i < num_nodes_in_layer_hidden; i++) // loops through nodes in hidden layer 
		{
			b = biases_1;
			//System.out.println(Arrays.toString(biases_1));
			z = 0; // resets z for each node
				
			for (int j = 0; j < num_nodes_in_layer_input; j++) // loops through weights attached to input layer nodes
			{
				z += weights_01[i][j] * a0[j];
				
			}
			
			z += b[i];		
			a1[i] = 1 / (double)(1 + Math.pow(2.71828, -z)); // applies sigmoid function to determine inputs into layer 2
		}
		
		/// Layer 1 to 2
		for (int i = 0; i < num_nodes_in_layer_output; i++) // loops through nodes in outer layer 
		{
			b = biases_2;
			z = 0; // resets z for each node
				
			for (int j = 0; j < num_nodes_in_layer_hidden; j++) // loops through weights attached to hidden layer nodes
			{
				z += weights_12[i][j] * a1[j];
				
			}
			z += b[i];		
			
			a2[i] = 1 / (double)(1 + Math.pow(2.71828, -z)); // applies sigmoid function to determine inputs into layer 2
		}
		
		int greatest_output = 0;
		
		// checks the greatest output and compares it to the label
		for (int i = 0; i < num_nodes_in_layer_output; i++)
		{
			if (a2[i] > a2[greatest_output])
			{
				greatest_output = i;
			}
		}
		
		if (y[greatest_output] == 1) // if the network chose the correct value for its output
		{
			correct_outputs[greatest_output]++;
		}
		
		cost = 0;
		// Calculates Cost
		for (int i = 0; i < num_nodes_in_layer_output; i++)
		{
			cost += Math.pow(y[i] - a2[i], 2);
		}
		cost *= .5;
	}
	
	static void BackwardPass(double[] a, int y[])
	{
		d1 = new double[num_nodes_in_layer_hidden];
		d2 = new double[num_nodes_in_layer_output];
		
		// Layer 1 to 2
		for (int i = 0; i < num_nodes_in_layer_output; i++) // loops through all nodes in outer layer
		{
			d2[i] = (a2[i] - y[i]) * a2[i] * (1 - a2[i]); // equation for error in Lth (final) layer (equation 1)
			bias_gradients_2[i] = d2[i]; // bias gradient = the error (equation 3)
			total_bias_gradients_2[i] += bias_gradients_2[i]; // adds current b gradient to sum of b gradients
			
			for (int j = 0; j < num_nodes_in_layer_hidden; j++)
			{
				weight_gradients_12[i][j] = a1[j] * bias_gradients_2[i]; // weight gradient = input * error (equation 4)
				total_weight_gradients_12[i][j] += weight_gradients_12[i][j]; // adds the current gradients to the gradient total that will determine new weights at end of minibatch
			}
		}
		
		// Layer 0 to 1
		for (int i = 0; i < num_nodes_in_layer_hidden; i++) // loops through all nodes in hidden layer
		{
			d1[i] = 0;
			
			for (int j = 0; j < num_nodes_in_layer_output; j++) // loops through nodes in output layer to apply summation of weights and errors (equation 2)
			{
				d1[i] += weights_12[j][i] * d2[j];
			}
			
			d1[i] *= (a1[i] * (1-a1[i])); // applies the second half of the l layer equation (equation 2)
			bias_gradients_1[i] = d1[i]; // bias gradient = the error (equation 3)
			total_bias_gradients_1[i] += bias_gradients_1[i]; // adds current b gradient to sum of b gradients
			
			for (int k = 0; k < num_nodes_in_layer_input; k++)
			{
				weight_gradients_01[i][k] = a[k] * bias_gradients_1[i];
				total_weight_gradients_01[i][k] += weight_gradients_01[i][k]; // adds the current gradients to the gradient total that will determine new weights at end of minibatch
			}
		}	
	}
	
	static void ReviseWeightsAndBiases()
	{
		for (int i = 0; i < num_nodes_in_layer_hidden; i ++) // applies new weights and biases to hidden layer
		{
			biases_1[i] = biases_1[i] - (eta/2) * total_bias_gradients_1[i]; // new bias
			
			for (int j = 0; j < num_nodes_in_layer_input; j++) 
			{
				weights_01[i][j] = weights_01[i][j] - (eta/2) * total_weight_gradients_01[i][j]; // new weight
			}
		}

		for (int i = 0; i < num_nodes_in_layer_output; i++) // applies new weights and biases to output layer
		{
			biases_2[i] = biases_2[i] - (eta/2) * total_bias_gradients_2[i]; // new bias
			
			for (int j = 0; j < num_nodes_in_layer_hidden; j++)
			{
				weights_12[i][j] = weights_12[i][j] - (eta/2) * total_weight_gradients_12[i][j]; // new weight
			}
			
		}
		
	}
	
	static void TrainingLoop()
	{
		int num_of_epochs = 30;
		
		for (int i = 0; i < input_size; i++) // creates array of indices that will be randomized to determine minibatches
		{
			indices.add(i);
		}
		
		for (int i = 0; i < num_of_epochs; i++) // loops over each epoch
		{
			Collections.shuffle(indices); // shuffles indices array
			for (int j = 0; j < num_nodes_in_layer_output; j++)
			{
				correct_outputs[j] = 0; // cleans correct output array for each epoch
			}
			
			for (int j = 0; j < input_size / minibatch_size; j++ ) // loops over each minibatch in the epoch
			{
				DetermineMinibatch(j);
				
				WipeGradients();
				
				for (int k = 0; k < minibatch_size; k ++) // loops over all training cases in the minibatch
				{				
					ForwardPass(minibatch_values[k], minibatch_labels[k]);					
					BackwardPass(minibatch_values[k], minibatch_labels[k]);				
				}		
				
				ReviseWeightsAndBiases();
			}
			int total_correct = 0;
			int total = input_size;
			
			for (int j = 0; j < num_nodes_in_layer_output; j++) // adds all correct outputs together
			{
				total_correct += correct_outputs[j];
			}
			
			double accuracy = ((float)total_correct / total) * 100;
			
			// Outputs statistics for each epoch
			System.out.println("Epoch " + i);
			System.out.println("0 = " + correct_outputs[0] + "/" + total_outputs[0]);
			System.out.println("1 = " + correct_outputs[1] + "/" + total_outputs[1]);
			System.out.println("2 = " + correct_outputs[2] + "/" + total_outputs[2]);
			System.out.println("3 = " + correct_outputs[3] + "/" + total_outputs[3]);
			System.out.println("4 = " + correct_outputs[4] + "/" + total_outputs[4]);
			System.out.println("5 = " + correct_outputs[5] + "/" + total_outputs[5]);
			System.out.println("6 = " + correct_outputs[6] + "/" + total_outputs[6]);
			System.out.println("7 = " + correct_outputs[7] + "/" + total_outputs[7]);
			System.out.println("8 = " + correct_outputs[8] + "/" + total_outputs[8]);
			System.out.println("9 = " + correct_outputs[9] + "/" + total_outputs[9]);
			System.out.println("Accuracy = " + total_correct + "/" + total + " = " + accuracy + "%");
			System.out.println();
		}
	}
	
	static void TestingLoop()
	{
		correct_outputs = new int[num_nodes_in_layer_output];
		
		for (int i = 0; i < input_size; i++)
		{
			ForwardPass(value[i], label[i]); // only foreward pass on each input
		}
	
		int total_correct = 0;
		int total = input_size;
		
		for (int j = 0; j < num_nodes_in_layer_output; j++) // adds all correct outputs together
		{
			total_correct += correct_outputs[j];
		}
		double accuracy = ((float)total_correct / total) * 100;
		
		System.out.println();
		System.out.println("Accuracy on Testing Set");
		System.out.println("0 = " + correct_outputs[0] + "/" + total_outputs[0]);
		System.out.println("1 = " + correct_outputs[1] + "/" + total_outputs[1]);
		System.out.println("2 = " + correct_outputs[2] + "/" + total_outputs[2]);
		System.out.println("3 = " + correct_outputs[3] + "/" + total_outputs[3]);
		System.out.println("4 = " + correct_outputs[4] + "/" + total_outputs[4]);
		System.out.println("5 = " + correct_outputs[5] + "/" + total_outputs[5]);
		System.out.println("6 = " + correct_outputs[6] + "/" + total_outputs[6]);
		System.out.println("7 = " + correct_outputs[7] + "/" + total_outputs[7]);
		System.out.println("8 = " + correct_outputs[8] + "/" + total_outputs[8]);
		System.out.println("9 = " + correct_outputs[9] + "/" + total_outputs[9]);
		System.out.println("Accuracy = " + total_correct + "/" + total + " = " + accuracy + "%");
		System.out.println();
	}
	
	static void LoadNetworkState() throws IOException
	{
		@SuppressWarnings("resource")
		BufferedReader csvReader = new BufferedReader(new FileReader("networkstate.txt"));
		
		String data;
		
		while ((data = csvReader.readLine()) != null) // loops through each weight and bias
		{
			String[] data_arr = data.split(",");
			int index = 0;
			
			// saves all weights from input layer to hidden layer
			for (int i = 0; i < num_nodes_in_layer_hidden; i++)
			{
				for (int j = 0; j < num_nodes_in_layer_input; j++)
				{
					weights_01[i][j] = Double.valueOf(data_arr[index]);
					index ++;
				}			
			}
			
			for (int i = 0; i < num_nodes_in_layer_output; i++)
			{
				for (int j = 0; j < num_nodes_in_layer_hidden; j++)
				{
					weights_12[i][j] = Double.valueOf(data_arr[index]);
					index ++;
				}			
			}
			
			for (int i = 0; i < num_nodes_in_layer_hidden; i++)
			{
				biases_1[i] = Double.valueOf(data_arr[index]);
				index ++;		
			}
			
			for (int i = 0; i < num_nodes_in_layer_output; i++)
			{
				biases_2[i] = Double.valueOf(data_arr[index]);
				index ++;		
			}
		}
	}
	
	static void SaveNetworkState() throws FileNotFoundException
	{
		o = new PrintStream("networkstate.txt");
		console = System.out;
		System.setOut(o); // program outputs to .txt file
		
		// saves all weights from input layer to hidden layer
		for (int i = 0; i < num_nodes_in_layer_hidden; i++)
		{
			for (int j = 0; j < num_nodes_in_layer_input; j++)
			{
				System.out.print(weights_01[i][j]);
				System.out.print(",");
			}			
		}
		
		// saves all weights from hidden layer to output layer
		for (int i = 0; i < num_nodes_in_layer_output; i++)
		{
			for (int j = 0; j < num_nodes_in_layer_hidden; j++)
			{
				System.out.print(weights_12[i][j]);
				System.out.print(",");
			}			
		}
		
		// saves all biases for hidden layer
		for (int i = 0; i < num_nodes_in_layer_hidden; i++)
		{
			System.out.print(biases_1[i]);
			System.out.print(",");
		}
		
		// saves all biases for output layer
		for (int i = 0; i < num_nodes_in_layer_output; i++)
		{
			System.out.print(biases_2[i]);
			System.out.print(",");
		}
		
		System.setOut(console); // changes output stream back to console
	} 

	public static void main(String args[]) throws IOException 
	{
		
		input_size = 60000;
		
		label = new int[input_size][10];
		value = new double[input_size][784];
		
		minibatch_size = 10;
		num_of_minibatches = input_size / minibatch_size;
		minibatch_labels = new int[minibatch_size][10];
		minibatch_values = new double[minibatch_size][784];
		
		num_nodes_in_layer_input = 784;
		num_nodes_in_layer_hidden = 30;
		num_nodes_in_layer_output = 10;
		
		weights_01 = new double[num_nodes_in_layer_hidden][num_nodes_in_layer_input];
		weights_12 = new double[num_nodes_in_layer_output][num_nodes_in_layer_hidden];
		biases_1 = new double[num_nodes_in_layer_hidden];
		biases_2 = new double[num_nodes_in_layer_output];
		weight_gradients_01 = new double[num_nodes_in_layer_hidden][num_nodes_in_layer_input];
		weight_gradients_12 = new double[num_nodes_in_layer_output][num_nodes_in_layer_hidden];
		bias_gradients_1 = new double[num_nodes_in_layer_hidden];
		bias_gradients_2 = new double[num_nodes_in_layer_output];
		total_bias_gradients_1 = new double[num_nodes_in_layer_hidden];
		total_bias_gradients_2 = new double[num_nodes_in_layer_output];
		total_weight_gradients_01 = new double[num_nodes_in_layer_hidden][num_nodes_in_layer_input];
		total_weight_gradients_12 = new double[num_nodes_in_layer_output][num_nodes_in_layer_hidden];
		total_outputs = new int[num_nodes_in_layer_output];
		correct_outputs = new int[num_nodes_in_layer_output];
		
		Scanner scan = new Scanner(System.in);
		System.out.println("Welcome to the MNIST Neural Network. Please Enter your command");
		String c = scan.nextLine();
		int command = Integer.valueOf(c);
		
		if (command == 1 || command == 2 || command == 0 ) // only enter loop if initial commands are 1 or 2
		{
			
			while(true)
			{
				switch (command)
				{
					case 1: // train the network
						GenerateRandomWeightsAndBiases();
						eta = 3;					
						indices = new ArrayList<Integer>();						
						System.out.println("Now Scanning Input File");
						ReadInputFile(false);				
						System.out.println("File Input Read");						
						System.out.println("Beginning Training Now");
						TrainingLoop();
						System.out.println("Network Trained");
						break;
						
					case 2: // load a pre trained network from a file
						System.out.println("Loading Pre-Trained Network Now");
						LoadNetworkState();
						System.out.println("Pre-Trained Network Loaded");
						break;
						
					case 3: // display accuracy on training set
						System.out.println("Now Scanning Input File");
						ReadInputFile(false);
						System.out.println("Testing Network on Training Set");
						TestingLoop();
						System.out.println("Network Tested");
						break;
						
					case 4: // display accuracy on testing set
						input_size = 10000;
						System.out.println("Now Scanning Input File");
						ReadInputFile(true);
						System.out.println("Testing Network on Testing Set");
						TestingLoop();
						System.out.println("Network Tested");
						break;
					
					case 5: // save network state
						System.out.println("Saving Network State to File");
						SaveNetworkState();
						System.out.println("Network State Saved");
						break;
						
					case 0: // goodbye!
						System.out.println("Goodbye!");
						System.exit(0);
						break;
						
				}
				
				System.out.println("Please Enter your next command");
				c = scan.nextLine();
				command = Integer.valueOf(c);				
			}
		}			
	}
}