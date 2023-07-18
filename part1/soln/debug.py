import os
from util import *

if __name__ == "__main__":

    task = input("Task (height or weight): ")
    assert(task in ["height", "weight"]), "Invalid task. Choose from height or weight."

    data_file = "data.csv"
    class_file = f"{task}.txt"
    feature_name = "country"

    df = get_data(data_file, feature_name, class_file)


    country = input("Country (Australia, USA or Japan): ")
    
    c1 = df[(df['country'] == country) & (df['class'] == 1)]
    print(f"Number with {task} greater than mean: {len(c1)}")