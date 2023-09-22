import os


class Datasets: 
    def __init__(self, path):
        self.path = path



    def possible_models(self):
        path = self.path

        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                print(file_path)

    ## Transcripts
    def load_whole_transcript(self, model):
        path = self.path

        if ".txt" in model:
            for file_name in os.listdir(path):
                if file_name == model:
                    target_file_path = os.path.join(path, model)
                    with open(target_file_path, 'r') as file:
                        file_contents = file.read()


                    return file_contents
            
            
            else:
                return "File not found in the specified folder."

    
    ## Character's
    def save_character(model, output_dir, character):
        lines = []
    
        with open(f"{model}", 'r') as source_flie:
            for line in source_flie:
                if character in line:
                    lines.append(line)
    
        if lines:
            with open(f"Characters/{output_dir}", 'w') as output:
                for line in lines:
                    output.write(line)
                    return f"{character} saved in {output}"


    def load_character(dataset):
        data = []
    
        with open(f"Characters/{dataset}", 'r') as source_file:
            for line in source_file:
                data.append(line)
    
        return data