MODEL:=rnn_model.keras
TRAINING_SET:=data

all:	generate train predict

generate:	${TRAINING_SET}

train:	${MODEL}

${MODEL}:	train.py ${TRAINING_SET}
	./$<

predict:
	bash -c "./predict.py | grep -v step | while read ANS ; do echo \$$ANS ; sleep 0.1 ; done" | ./driveGnuPlots.pl 3 150 150 150 Actual Predicted Delta

${TRAINING_SET}:	generator.py
	./$< > $@

clean:
	rm -f ${TRAINING_SET} ${MODEL}

.PHONY: generate visualize predict clean
