import argparse

import gym

parser = argparse.ArgumentParser(description="test env")
parser.add_argument(
    "--env_name", type=str, default="CartPole-v0", help="env name"
)
parser.add_argument("--test_times", type=int, default=10, help="test times")
parser.add_argument("--render", action="store_true", help="env render")


def test(args):
    env = gym.make(args.env_name)
    for i in range(args.test_times):
        env.reset()
        for _ in range(1000):
            if args.render:
                env.render()
            action = env.action_space.sample()  # take a random action
            observation, reward, done, info = env.step(action)
            if done:
                print(f"{i+1} done!!!!")
                break
    env.close()


if __name__ == "__main__":
    args = parser.parse_args()
    test(args)
