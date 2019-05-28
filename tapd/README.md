# The reference code comes from https://github.com/ciwang/policydistillation

 # Two key variables:
 
 gen: the generation of student, gen=0 denotes teacher model, gen=1 denotes the first generation model, etc.
 
 size1, size2, size3, size4(natureqn.py): sizes of all layers, change them manually according "gen"
 
Example for "Quick" start:
- Train Teacher model : Run ```python natureqn_atari.py```  Make sure "gen=0"

- Train the first generation student model :Run ```python distilledqn_atari.py```, makesure gen=1 by setting "model = DistilledQN(env, config, gen =1)"

- Train the second generation student model: Run ```python distilledqn_atari.py```, makesure gen=1 by setting "model = DistilledQN(env, config, gen =2)", don't forget to change sizes in "natureqn.py"
