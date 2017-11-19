import numpy as np

# learning rate value

learn_rate = 0.01

# Input pretended target

target_value = input("Insert the number value of your target: ")

# turn input str into integer

target_value = int(target_value)

# number of epochs
epochs = input("Insert the number of cicles( Remember, the more ammount of cicles you have, more accurate the result will be ): ")

# turn input str into integer

epochs = int(epochs)

# input data values

input_data = np.array([2,3])

# weight values

weights = np.array([3,4])

# predicted value (output value)

output_data = (input_data * weights).sum()

error = output_data - target_value

print("The error is: ",error)
print("First output value is: ",output_data)
# until the error is no longer non-existended


for x in range(0, epochs):
    slope = 2 * input_data * error

    weights = weights - ( learn_rate * slope )

    output_data = (input_data * weights).sum()

    error = output_data - target_value
    print("The error is: ",error)  
    print("Predicted value is: ",output_data)
print("It worked")