import os
import argparse

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('--exp-id', default=0, type=int)
	return parser.parse_args()
# exp-id 0,1 simple_push_modified good:maddpg, bad: maddpg

if __name__ == '__main__':
	args = parse_arguments()
	envs = ["simple_push_modified"]
	for env in envs:
		print("************************")
		print("Running on {}.".format(env))
		print("************************")
		cmd = "python train.py --scenario {}".format(env)
		cmd += " --num-episodes {}".format(240000)
		cmd += " --exp-id {}".format(args.exp_id)
		cmd += " --num-units 64"
		cmd += " --num-adversaries 1"
		os.system(cmd)