from environment.sts_env import STSEnv
from ai.inference.agent import RandomAgent


def main():

    env = STSEnv()

    agent = RandomAgent(env.action_space)

    state = env.reset()

    done = False

    while not done:

        action = agent.act(state)

        state, reward, done, _ = env.step(action)

        env.render()

    print("Reward:", reward)


if __name__ == "__main__":
    main()