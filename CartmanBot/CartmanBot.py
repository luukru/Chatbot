import seq2seq.data as data
import seq2seq.data_utils as data_utils
import seq2seq.seq2seq_wrapper as seq2seq_wrapper

class CartmanBot:

    def __init__(self):
        self.metadata = []
        self.vocabulary = []
        self.model = self.initialize_model()
        self.sess = self.model.restore_last_session()

    def initialize_model(self):
        print("Initializing model...")
        
        import importlib
        importlib.reload(data)

        self.metadata, idx_q, idx_a = data.load_data(PATH='')
        (trainX, trainY), (testX, testY), (validX, validY) = data_utils.split_dataset(idx_q, idx_a)

        self.vocabulary = self.metadata['idx2w']

        xseq_len = trainX.shape[-1]
        yseq_len = trainY.shape[-1]
        batch_size = 16
        xvocab_size = len(self.metadata['idx2w'])  
        yvocab_size = len(self.metadata['idx2w'])  
        emb_dim = 1024

        model = seq2seq_wrapper.Seq2Seq(xseq_len=xseq_len,
                               yseq_len=yseq_len,
                               xvocab_size=xvocab_size,
                               yvocab_size=yvocab_size,
                               ckpt_path='ckpt/',
                               emb_dim=emb_dim,
                               num_layers=3,
                                epochs=100000)

        return model

    def send_greeting(self):
        return "Hello there! CartmanBot here... feel free to ask me any question and I will try to answer you as best as possible."
    
    def generate_reply(self, input_):
        input_ = data.process_input(input_, self.vocabulary, self.metadata) # preprocess data
        output = self.model.predict(self.sess, input_)
        # Try all possible outputs, from highest predicted rank to lower
        for i, oi in enumerate(output):
            decoded_output = data_utils.decode(sequence=output[i], lookup=self.metadata['idx2w'], separator=' ').split(' ')
            print(decoded_output)
            if 'unk' not in decoded_output:
                return ' '.join(decoded_output)                
        # Return the first output if no output without unknown words is found
        return ' '.join(data_utils.decode(sequence=output[0], lookup=self.metadata['idx2w'], separator=' ').split(' '))
