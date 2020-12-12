from collections import Counter
import random



random.seed(2020)
def random_number_list():
    random_20_num_list = []
    for _ in range(20):
        random_20_num_list.append(random.randint(100,120))
    return random_20_num_list    


if __name__ == "__main__":
    generated_num_list = random_number_list()
    print(f"The randomly generated numbers are {', '.join(map(str, generated_num_list))}.")
    print()

    #Calculate Median which is the 10th largest number.
    median = sorted(generated_num_list)[len(generated_num_list)//2]
    print(f"Median of generated numbers is {median}")

    #Calculate Mode or Multi-mode as per generated list.
    numbers_count_dict = Counter(generated_num_list)
    mode = [k for k, v in numbers_count_dict.items() if v == max(list(numbers_count_dict.values()))]
    print(f"Mode of generated numbers is/are {','.join(map(str, mode))}")    
   