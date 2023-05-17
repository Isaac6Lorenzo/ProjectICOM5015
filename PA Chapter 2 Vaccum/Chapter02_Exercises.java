import java.util.ArrayList;
import java.util.List;

import aima.core.agent.Action;
import aima.core.agent.Agent;
import aima.core.agent.EnvironmentListener;
import aima.core.agent.impl.AbstractEnvironment;
import aima.core.agent.impl.SimpleEnvironmentView;
import aima.core.environment.vacuum.MazeVacuumEnvironment;
import aima.core.environment.vacuum.RandomWalkVacuumAgent;
import aima.core.environment.vacuum.ReflexVacuumAgent;
import aima.core.environment.vacuum.VacuumEnvironment;
import aima.core.environment.vacuum.VacuumPercept;


//Isaac L. Rodríguez Pacheco
//Román J. Rosario Recci
//Alicia C. Garcia Reyes
//Group H 

//Prof. J. Fernando Vega Rivero
//ICOM 5015 - 001D
//March 6, 2023


public class Chapter02_Exercises {

	public static void main(String[] args) {

		VacuumEnvironment.LocationState Dirty = VacuumEnvironment.LocationState.Dirty;
		VacuumEnvironment.LocationState Clean = VacuumEnvironment.LocationState.Clean;

		//Exercise 2.11 (Ex. 2.8)
		System.out.println("Reflex Agent with two location, they are clean or dirty, then suck if dirty");
		System.out.println("Loc A: D, Loc B: D");
		ReflexAgent(Dirty, Dirty);
		System.out.println("----------------------------------------------------------------");
		System.out.println("Loc A: D, Loc B: C");
		ReflexAgent(Dirty, Clean);
		System.out.println("----------------------------------------------------------------");
		System.out.println("Loc A: C, Loc B: D");
		ReflexAgent(Clean, Dirty);
		System.out.println("----------------------------------------------------------------");
		System.out.println("Loc A: C, Loc B: C");
		ReflexAgent(Clean, Clean);
		System.out.println("----------------------------------------------------------------");
		System.out.println("----------------------------------------------------------------");

		//Exercise 2.14 (Ex. 2.11)
		System.out.println("----------------------------------------------------------------");
		System.out.println("ReflexAgent with Random Walk");
		int xdim = 5;
		int ydim = 5;
		double dirtProbability = 0.50; //between 0.00 to 0.99 or 1.0 in percent * 100%
		double obstacleProbability = 0;
		ReflexAgent_RandomWalk(xdim, ydim, dirtProbability, obstacleProbability);
		System.out.println("----------------------------------------------------------------");

		//for debugging
		//		List<Double> list = new ArrayList<Double>(5);
		//		for (int i = 0; i < 10; i++) {
		//			list.add(ReflexAgent_RandomWalk(xdim, ydim, dirtProbability, obstacleProbability));
		//		}
		//
		//		for (Double num : list) {
		//			System.out.println("Performance: " + num);
		//		}


	}



	//Exercise 2.11 (Ex. 2.8)
	public static void ReflexAgent(VacuumEnvironment.LocationState A, VacuumEnvironment.LocationState B) {
		String LocA = VacuumEnvironment.LOCATION_A;
		String LocB = VacuumEnvironment.LOCATION_B;
		List<String> locations = new ArrayList<String>();
		VacuumEnvironment.LocationState[] locStates = new VacuumEnvironment.LocationState[2];
		locations.add(LocA);
		locations.add(LocB);
		locStates[0] = A;
		locStates[1] = B;

		AbstractEnvironment<VacuumPercept, Action> env = new VacuumEnvironment(locations, locStates);
		EnvironmentListener<Object, Object> view = new SimpleEnvironmentView();
		env.addEnvironmentListener(view);

		Agent<VacuumPercept, Action> agent = new ReflexVacuumAgent();
		env.addAgent(agent);
		boolean clean_A = false;
		boolean clean_B = false;

		if(check(env, clean_A, clean_B, agent) == true) {
			env.executeNoOp(agent);
		}

		System.out.println("Finish: " + env.isDone());
		env.notify("Performance=" + env.getPerformanceMeasure(agent));

	}

	//Exercise 2.14 (Ex. 2.11)
	public static double ReflexAgent_RandomWalk(int xdim,	int ydim, 
			double dirtProbability, double obstacleProbability) {

		MazeVacuumEnvironment maze = new MazeVacuumEnvironment(xdim, ydim, 
				dirtProbability, obstacleProbability);
		EnvironmentListener<Object, Object> view = new SimpleEnvironmentView();
		Agent<VacuumPercept, Action> agent = new RandomWalkVacuumAgent();
		maze.addEnvironmentListener(view);
		maze.addAgent(agent);

		List<String> location_list = maze.getLocations();
		int locSize = location_list.size();
		int count_true = 0;

		while(count_true != locSize) {
			maze.step();
			count_true = 0;
			for (int i = 0; i < locSize; i++) {
				String loc = location_list.get(i);
				VacuumEnvironment.LocationState state = maze.getLocationState(loc);
				if(VacuumEnvironment.LocationState.Clean == state) {
					count_true++;
				}

			}

		}

		if(count_true == locSize) {
			maze.executeNoOp(agent);
		}





		System.out.println("Finish: " + maze.isDone());
		maze.notify("Performance=" + maze.getPerformanceMeasure(agent));

		return maze.getPerformanceMeasure(agent);


	}




	//method to check if both locA and locB are clean 
	public static boolean check(AbstractEnvironment<VacuumPercept, Action> env, boolean clean_A, boolean clean_B, Agent agent) {
		while(clean_A == false || clean_B == false) {
			if (env.getPerceptSeenBy(agent).getCurrLocation() == VacuumEnvironment.LOCATION_A && 
					env.getPerceptSeenBy(agent).getCurrState() == VacuumEnvironment.LocationState.Clean) {
				env.step();
				clean_A = true;
			}

			if (env.getPerceptSeenBy(agent).getCurrLocation() == VacuumEnvironment.LOCATION_B && 
					env.getPerceptSeenBy(agent).getCurrState() == VacuumEnvironment.LocationState.Clean) {
				env.step();
				clean_B = true;
			}

			else
				env.step();
		}

		if(clean_A && clean_B) {
			return true;
		}

		return false;
	}

}
