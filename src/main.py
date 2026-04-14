import gymnasium as gym

env = gym.make("LunarLander-v3")

obs, info = env.reset()

while True:
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, info = env.reset()
    env.render()

env.close()