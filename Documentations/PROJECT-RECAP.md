# Start trek : Project recap

#### Goal : training a module to land by itself

> binary name : \*.py
> language : Python
> authorized librairies: gymnasium, pytorch

### Sum-up of theproject :

You will program an algorithm that enables the modules to correct its own trajectory.
It wille be a reinforcement-learning agent that learns by trials and error from sparse rewards.
You will emphasiez the RL loop (state -> action -> reward), exploration-exploitation trade-offs, and basic value/Q estimation before any deep networks.
Success is measured by consistent autonomous landings and improved sample-efficiency across iterations.
You will build a disciplined engineering habits (metrics, reproducibility, readable code).
You will delivered a detailed report provide evidence of your tests, explain your modification, and defenc, with structural and functional arguments your solution.

---

### Use of gymnasium:

an API standard for RL, using Lunar Lander

[Gymnasium Documentation](https://gymnasium.farama.org/index.html)

### Possible action of the lunar lander :

* do nothing
* fire left thruster
* fire main engine
* fire right thruster

continuous-control is possible

### State : 8 dimensional vector :

* x : horizontal position
* y : vertical position
* v_x : horizontale velocity
* v_y : vertical velocity
* theta : lander angle
* theta_dot : angular velocity
* left_leg_contact : bool : 1 if l-in contact with the ground else 0
* right_leg_concat : same as the left one

### Reward :

reward shaping is used, the reward function encourage :

* being close to the landing pad
* moving slowly
* staying level (lander kept horizontal)

there are also:

* per-step penalties when engines are firing
* about +100 for a safe landing
* about -100 for a crash

note : the environment is considered solved when the mean scored is greater than or equal to 200 (without wind which is considered a bonus)

## Usage of Gymnasium

```python
import gymnasium as gym

env = gym/make("LunarLander-v3", render_mode="rgb_array") # discrete by default
obs, info = env.reset(seed=SEED)

while True:
    action = policy(obs) #random or learned
    obs, r, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, info = env.reset()
```

For continious control or wind:

```
gym.make("LunarLander-v3", continuous=True, enable_wind=True, wind_power=15.0, turbulence_power=1.5()
```

## Goals

### Deliverables

* Codebase (clean repo; train.py, eval.py; README)
* YAML configs for each run (env, algo, hypers, seeds)
* Tracking 1 assets : returns/episode length plots, termination cause starts, videos
* Short report (4-6 pages) : setup, results, 1>= ablation, limits next steps.
* One-click repro script to regenrate figures + CSV

### Tasks

1. Baseline & instrumentation
   1. Random policy and a simple heuristic, log returns, episode length, why it ended (crash/out-of-view/sleep). Save videos
2. Agent (discrete)
   1. MLP (2-3xReLU), replay, target net, epsilon-greedy decay, Plot returns, epsilon, loss.
3. Ablation (>= 1)
   1. e.g., buffer siez, hard vs soft target updates; observation normalization, reward clipping.
4. Reproductability
   1. \>= 5 seeds (0..4), report mean +/- 95% CI for key metrics
5. Defense
   1. Student must be abale to justify their choices, benchmark different techniques and talk about their reasoning

---

### Acceptance criteria

* achieve mean score >= 200 over 100 consecutive episodes (report distribution & variance)
* correctly handle and log terminated VS truncated and the termination reason (crash, out-of-view, sleep)
* one-click repro regenerates the same plots/CSV within =/-5% with the same seeds/configs