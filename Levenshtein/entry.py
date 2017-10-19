import standard_levenshtein as standard
import modified_levenshtein as modified
import levenshtein_with_recursion as recursion

if __name__ == "__main__":
    first_string = input("Enter the first string: ")
    second_string = input("Enter the second string: ")

    print("Levenshtein distance between the entered words: \n",
          standard.levenshtein_distance(first_string, second_string),
          modified.modified_levenstein(first_string, second_string),
          recursion.levenshtein_disctance_recursion(first_string, second_string))
