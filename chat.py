import os # operating system

def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            line = line.strip()
            products.append(line)
    return products

def write_file(products):
    with open('output.txt', 'w', encoding = 'utf-8') as f:    
        for p in products:
            if 'Allen' in p:
                person = 'Allen'
                continue
            elif 'Tom' in p:
                person = 'Tom'
                continue
            elif person == 'Allen':    
                f.write('Allen: ' + str(p) + '\n')
            elif person == 'Tom':
                f.write('Tom: ' + str(p) + '\n')
                
            
def main():
    filename = 'input.txt'
    if os.path.isfile(filename): # 檢查檔案在不在
        print('yeah! 找到檔案了!')
        products = read_file(filename)
        write_file(products)
    else:
        print('找不到檔案......')
    

main()         