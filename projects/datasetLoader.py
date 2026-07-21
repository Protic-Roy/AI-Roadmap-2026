class TextDataset:
    def __init__(self, sentences):
        self.sentences = sentences
    
    def __len__(self):
        return len(self.sentences)
    
    def __getitem__(self, idx):
        return self.sentences[idx]