conda activate llm311

# Install critical binary deps via conda
conda install -y numpy=1.26 pytorch cpuonly -c pytorch

# Then install the rest via pip
pip install -r requirements.txt
