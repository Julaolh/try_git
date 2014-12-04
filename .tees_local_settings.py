
# Edit these settings to configure TEES. A variable must have a value 
# other than None for it to be usable. This file is interpreted as
# a Python module, so Python code can be used.

# Tools
SVM_MULTICLASS_DIR = None # svm_multiclass_learn and svm_multiclass_classify directory
BANNER_DIR = None # BANNER program directory
GENIA_SENTENCE_SPLITTER_DIR = None # GENIA Sentence Splitter directory
RUBY_PATH = "ruby" # Command to run Ruby (used only by the GENIA Sentence Splitter)
BLLIP_PARSER_DIR = None # The BLLIP parser directory
MCCLOSKY_BIOPARSINGMODEL_DIR = None # The McClosky BioModel directory
STANFORD_PARSER_DIR = None # The Stanford parser directory

# Data
DATAPATH = 'C:\BioNER\Tees_root/.tees' # Main directory for datafiles
CORPUS_DIR = None # Directory for the corpus XML-files
MODEL_DIR = None # Directory for the official TEES models
