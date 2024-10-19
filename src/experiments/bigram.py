import argparse
# import torch

def data_from_file(file):
    data = open(file, 'r').read().splitlines()
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True, default='names.txt')
    
    args = parser.parse_args()
    
    names = data_from_file(file=args.data)

    chars = sorted(set(''.join(names)))
    string_to_idx = {string:idx+1 for idx, string in enumerate(chars)}
    string_to_idx['<S>'] = 26
    string_to_idx['<E>'] = 27
    print(string_to_idx)
        
    idx_to_string = {idx:string for string, idx in string_to_idx.items()}
    print(idx_to_string)
    bigrams = dict()
    
    for name in names[:3]:
        chars = ['<S>'] + list(name) + ['<E>']
        for char_1, char_2 in zip(chars, chars[1:]):
            idx_1 = string_to_idx.get(char_1)
            idx_2 = string_to_idx.get(char_2)
            print(idx_1, idx_2)
            bigram = (char_1, char_2)
            bigrams[bigram] = bigrams.get(bigram, 0) + 1
            # print(char_1, char_2)
    
    # print(bigrams)
            

    