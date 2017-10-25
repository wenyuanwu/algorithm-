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

