#!/bin/bash


node="412"
job_name="job1-${node}"
currentTime=`date "+%Y-%m-%d %H:%M:%S"`

echo "#!/bin/sh
#\$-q datasci
#\$-q datasci3
#\$-N ${job_name}
#\$-cwd

cd ..
" > ${job_name}.sh

echo "
echo 'job name: ${job_name}
TimeStamp: ${currentTime}'
#python evaluate.py --source mnist_scd_v9.pkl --type mode
#python evaluate.py --source mnist_scd_v15.pkl --type mode
echo 'hello, world'
" > ${job_name}.contents
cat ${job_name}.contents >> ${job_name}.sh
cat ${job_name}.contents >> jobs.LOG
qsub -l hostname=node${node} ${job_name}.sh
rm ${job_name}.contents
rm ${job_name}.sh

