#!/bin/bash
#SBATCH --job-name=CI2          #job name
#SBATCH --nodes=1             # Number of nodes
#SBATCH --ntasks=1            # Number of cores
#SBATCH --output=/n/home04/lvanson/SFRD_fit/src/data//slurm_out/CI2.out            # output storage file
#SBATCH --error=/n/home04/lvanson/SFRD_fit/src/data//slurm_out/CI2.err             # error storage file
#SBATCH --time=1:00:00              # Runtime in minutes
#SBATCH --mem=120000               # Memory per cpu in MB (see also --mem-per-cpu)
#SBATCH -p demink,conroy,hernquist,shared
#SBATCH --mail-user=aac.van.son@gmail.com         # Send email to user
#SBATCH --mail-type=FAIL       #
#
#Print some stuff on screen
echo $SLURM_JOB_ID
echo $SLURM_JOB_NAME
echo $SLURM_ARRAY_TASK_ID
#
#Set variables
export QT_QPA_PLATFORM=offscreen # To avoid the X Display error
#
cd /n/home04/lvanson/SFRD_fit/src/scripts//CosmicIntegration/
#
# Run your job
python FastCosmicIntegration.py  --path /n/home04/lvanson/SFRD_fit/src/data/ --filename COMPAS_Output_wWeights.h5 --outfname /RateData/2_Rate_info.h5 --mu0 0.015 --muz -0.049 --sigma0 1.129 --sigmaz 0.048 --alpha -1.778 --aSF 0.017 --bSF 1.481 --cSF 4.452 --dSF 5.913 --weight mixture_weight --zstep 0.01 --sens O3 --m1min 10. --dco_type BBH --redshiftBinSize 0.05 --maxzdet 0.5 > /n/home04/lvanson/SFRD_fit/src/data//slurm_out/CI2.log
    