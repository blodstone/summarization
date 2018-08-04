import argparse


class Opts:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Summarizer')

        dataset_type = parser.add_mutually_exclusive_group(required=True)
        dataset_type.add_argument('--amr', action='store_true', help='AMR dataset')
        # todo Implement DUC reader
        dataset_type.add_argument('--duc', action='store_true', help='DUC dataset')
        # todo Implement TAC reader
        dataset_type.add_argument('--tac', action='store_true', help='TAC dataset')

        parser.add_argument('-train_path', help='Training path.')
        parser.add_argument('-test_path', help='Test path.')
        parser.add_argument('-dev_path', help='Dev path.')

        parser.add_argument('-corpus_path', help='Path for corpus pickle files.')
        parser.add_argument('-output_path', help='Path for output files.')
        parser.add_argument('-model_path', help='Path for model files.')

        preprocessor = parser.add_argument_group('Preprocessor')
        preprocessor.add_argument('-corenlp_path', help='Stanford corenlp folder path', required=True)

        summarizer = parser.add_argument_group('Summarizer')
        summarizer.add_argument('-method', help='Summarizer method [lead]', default='lead')
        summarizer.add_argument('-n_lines',
                                help='Lead method hyper-parameter: number of lead lines.', type=int)

        evaluator = parser.add_argument_group('Evaluator')
        evaluator.add_argument('--rouge', action='store_true', help='ROUGE metric (R1, R2, RLCS)')
        self._args = parser.parse_args()

    @property
    def args(self):
        return self._args
