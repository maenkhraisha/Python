from pathlib import Path


# for file_path in Path.cwd().glob('*.txt'):    
#     new_path = Path('archive') / file_path.name
#     file_path.replace(new_path)


# print(f"You can find me here: {Path(__file__).parent}!")



path = Path(r"/home/maen/realpython/test.md")
path.name
path.parent
path.suffix
path.anchor
path.stem



# read the content of the file


full_string_path = __file__
path = Path(full_string_path)
path = path.parent / "test.txt"

with path.open(mode='r',encoding='utf-8') as f:
    print(f)
# with path.open(mode='r' , encoding='utf-8') as file:
#     content = file.read()
#     groceries = [line for line in content.splitlines if line.startswith("*")]
#     print(content)

# print("\n".join(groceries))

