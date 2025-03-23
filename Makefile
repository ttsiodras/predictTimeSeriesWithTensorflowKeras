all:	generate train predict

generate:	data

train:	rnn_model.keras

rnn_model.keras:	train.py data
	./$<

predict:
	bash -c "./predict.py | grep -v step | while read ANS ; do echo \$$ANS ; sleep 0.1 ; done" | ./driveGnuPlots.pl 3 150 150 150 Actual Predicted Delta

data:	generator.py
	./$< > $@

.PHONY: generate visualize predict
