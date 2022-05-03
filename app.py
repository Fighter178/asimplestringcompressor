import zlib, colorama, base64
colorama.init(convert=True) # Convert colors to allow it to work with the Windows Command Prompt/Console
def main():
    print('My Simple Computer Tools (String Compressor/Decompressor) v1.0')
    action = input('Would you like to compress (1) OR decompress (2) a string? : ')
    if action == '1' or action == '':
        string = input('Enter the string you want to compress (Meant for strings of 20+ characters) : ')
        level = input('Enter compression level (1-9, 1 is fast, but low ratio, 9 is slow, but high ration, default: 9) : ')
        if level == '':
            level = '9'
        level = int(level)
        compressed = base64.b64encode(zlib.compress(string.encode(), level))
        letters_saved = len(string) - len(compressed)
        bits_saved = letters_saved * 8 # Each ascii letter is 8 bits (1 byte)
        ratio = letters_saved / len(string)
        ratio = ratio*100
        ratio = round(ratio, 2)
        if letters_saved < 0:
            print(f'{colorama.Fore.YELLOW}WARNING: It seems that the compressed data is larger than the standard data, so you may want to use the standard data. This can happen if your string is very short, or there are very few reoccuring words/characters{colorama.Style.RESET_ALL}')
        print(f'{colorama.Fore.GREEN}Length before compression: {colorama.Style.RESET_ALL}{len(string)}')
        print(f'{colorama.Fore.LIGHTBLUE_EX}Length after compression: {colorama.Style.RESET_ALL}{len(compressed)}')
        print(f'{colorama.Fore.BLUE}Compression Level: {colorama.Style.RESET_ALL}{level}')
        print(f'{colorama.Fore.CYAN}Bits Saved: {colorama.Fore.GREEN}{bits_saved}{colorama.Style.RESET_ALL}')
        print(f'{colorama.Fore.CYAN}Characters Saved: {colorama.Fore.GREEN}{letters_saved}{colorama.Style.RESET_ALL}')
        print(f'{colorama.Fore.CYAN}Ratio: {colorama.Fore.GREEN}~{ratio}%{colorama.Style.RESET_ALL}')
        print(f'{colorama.Fore.BLUE}Compressed String (Byte Code): {colorama.Style.RESET_ALL}{compressed}')
        print(f'{colorama.Fore.BLUE}Compressed String (Standard): {colorama.Style.RESET_ALL}{compressed.decode()}')
        reset()
    elif action == '2':
        string = input('Enter the compressed string : ')
        decompressed = zlib.decompress(base64.b64decode(string))
        print(f'{colorama.Fore.GREEN}Length before decompression: {colorama.Style.RESET_ALL}{len(string)}')
        print(f'{colorama.Fore.LIGHTBLUE_EX}Length after decompression: {colorama.Style.RESET_ALL}{len(decompressed)}')
        print(f'{colorama.Fore.BLUE}Decompressed String (Byte Code): {colorama.Style.RESET_ALL}{decompressed}')
        print(f'{colorama.Fore.BLUE}Decompressed String (Standard): {colorama.Style.RESET_ALL}{decompressed.decode()}')
        reset()
    else: 
        print(f'{colorama.Fore.RED}ERROR:\n Unknown request: {action}. Use one of these: 1, 2')
def reset():
    resetq = input('Run program again (Y/N)')
    if resetq == '' or resetq == 'y':
        main()
    else: 
        raise SystemExit