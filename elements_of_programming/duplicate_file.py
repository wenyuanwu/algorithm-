import os

def find_duplicate_files(path):
	files_seen = {}
	stack = [path]

	duplicates = []

	while len(stack):
		current_path = stack.pop()

		if os.path.isdir(current_path):
			for path in os.listdir(current_path):
				full_path = os.path.join(current_path, path)
				stack.append(full_path)

		else:

			with open(current_path) as file:
				file_content = file.read()

			current_last_edited_time = os.path.getmtime(current_path)
				

