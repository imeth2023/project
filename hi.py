import random
import time

def generate_colorful_pattern():
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    reset = '\033[0m'
    
    while True:
        for _ in range(10):
            row = ''
            for _ in range(20):
                color = random.choice(colors)
                character = chr(random.randint(33, 126))
                row += f'{color}{character}{reset} '
            print(row)
            time.sleep(0.1)
        
        print('\n' * 10)

if __name__ == '__main__':
    generate_colorful_pattern()
