from transformers import AutoModel, AutoTokenizer

class LoadingModel(object):

    def __init__(self, pretrained_name):

        self.pretrained_name = pretrained_name

    def load(self):
        print("Downloading model...")
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path=self.pretrained_name)
        self.model = AutoModel.from_pretrained(pretrained_model_name_or_path=self.pretrained_name)
        
    def save(self):
        import os
        print("Saving model to disk...")
        current_folder = os.path.dirname(os.path.realpath(__file__))
        model_folder = os.path.join(current_folder, "model")
        self.tokenizer.save_pretrained(model_folder)
        self.model.save_pretrained(model_folder)
        print("Finished caching model!")

if __name__ == "__main__":

    load_model_bert = LoadingModel("VoVanPhuc/sup-SimCSE-VietNamese-phobert-base")
    load_model_bert.load()
    load_model_bert.save()