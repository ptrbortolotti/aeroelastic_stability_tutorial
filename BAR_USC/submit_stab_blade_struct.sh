#!/bin/bash
#SBATCH --account=bar
#SBATCH --time=1-00:00:00
#SBATCH --job-name=uscbs
#SBATCH --nodes=1
#SBATCH --mail-user pbortolo@nrel.gov
#SBATCH --mail-type BEGIN,END,FAIL
####SBATCH --partition=debug
#SBATCH --qos=high
######SBATCH --mem=1000GB      # RAM in MB
#SBATCH --output=job_log.%j.out  # %j will be replaced with the job ID

module purge
module load conda
module load comp-intel intel-mpi mkl
module unload gcc

source activate weis-stab

python stability.py 0 0 0
