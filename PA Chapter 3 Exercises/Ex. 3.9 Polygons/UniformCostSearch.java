
import java.awt.Color;
import java.util.*;

public class UniformCostSearch {
	
   public static void main(String[] args) {
   }
}
 
class Graph { //graph class
   private final Map<Point2D, Vertex> graph; 
   
      public static class Edge { //edge class
      public final Point2D v1; //points at either end of the edge
      public final Point2D v2;
      public final double dist; //distance between them
      public Edge(Point2D v1, Point2D v2, double dist) { //edge constructor
         this.v1 = v1;
         this.v2 = v2;
         this.dist = dist;
      }
      public String toString() { return ("(" + v1 + "," + v2 + ")\n");}
      public Point2D getp0(){ //getters for points
    	  return v1;
      }
      public Point2D getp1(){
    	  return v2;
      }

   }
 
  public static class Vertex implements Comparable<Vertex>{ 
	public final Point2D name; //vertex
	public double dist = Double.MAX_VALUE; //set initial dist to infinity 
	public Vertex previous = null; 
	public final Map<Vertex, Double> neighbours = new HashMap<>();
 
	public Vertex(Point2D name) //constructor
	{
		this.name = name;
	}

	private void printPath(List<Point2D> path) //prints path and adds to list
	{
		if (this == this.previous)
		{
			System.out.print(this.name); 
			path.add(this.name); //path is list in graph
		}
		else if (this.previous == null)
		{
			System.out.print(this.name + "(unreached)");
		}
		else
		{
			path.add(this.name); //recursive call
			this.previous.printPath(path);
			System.out.print(" -> " + this.name);

		}
	}
	
	public Point2D getPoint(){ //getter
		return name;
	}
	
	public double getDist(){ //getter
		return dist;
	}
 
	public int compareTo(Vertex other) //compare distances
	{
		if (dist == other.dist)
			return name.compareTo(other.name);
 
		return Double.compare(dist, other.dist);
	}
 
	@Override public String toString()
	{
		return "(" + name + ", " + dist + ")";
	}
}
 
   public Graph(Edge[] edges) { //edges array
      graph = new HashMap<>(edges.length);
 
      for (Edge e : edges) {
         if (!graph.containsKey(e.v1)) graph.put(e.v1, new Vertex(e.v1)); //checks if vertex already exists
         if (!graph.containsKey(e.v2)) graph.put(e.v2, new Vertex(e.v2));
      }
 
      for (Edge e : edges) {
         graph.get(e.v1).neighbours.put(graph.get(e.v2), e.dist);
         graph.get(e.v2).neighbours.put(graph.get(e.v1), e.dist); 
      }
   }
 
   public void uniformCost(Point2D startName) { //dijkstra algorithm
      final Vertex source = graph.get(startName); //set source
      NavigableSet<Vertex> queue = new TreeSet<>(); //create treeset
 
      for (Vertex v : graph.values()) { //init variables
         v.previous = v == source ? source : null;
         v.dist = v == source ? 0 : Double.MAX_VALUE;
         queue.add(v); //add to queue
      }
      uniformCost(queue); 
   }
 
   private void uniformCost(final NavigableSet<Vertex> queue) {      
      Vertex f, v;
      while (!queue.isEmpty()) { //for every vertex
 
         f = queue.pollFirst(); // vertex with smallest dist
         if (f.dist == Double.MAX_VALUE) break; 
         
         for (Map.Entry<Vertex, Double> map : f.neighbours.entrySet()) {
            v = map.getKey(); 
 
            final double alternateDist = f.dist + map.getValue();
            if (alternateDist < v.dist) { //id dist is shorter
               queue.remove(v); //remove and add
               v.dist = alternateDist;
               v.previous = f;
               queue.add(v);
            } 
         }
      } 
   }
   
   List<Point2D> path = new ArrayList<Point2D>(); //returns all possible paths
   List<Point2D> routes = new ArrayList<Point2D>(); //returns shortest route
   
   //graph functions that call vertex methods
   public void printPath(Point2D endName) { 
      graph.get(endName).printPath(path);
//      System.out.println();
   }

   public List<Point2D> getPath(){
	   return path; //path getter
   }

   public List<Point2D> getRoutes() { //route getter
      for (Vertex v : graph.values()) {
         routes.add(v.getPoint());
      }
      return routes;
   }
}


//references
//https://www.geeksforgeeks.org/convex-hull-using-graham-scan/
//https://algs4.cs.princeton.edu/99hull/GrahamScan.java.html

class GrahamScan { 

	public static void mergeSort(Comparable [ ] a) 
	{ 
		Comparable[] tmp = new Comparable[a.length]; 
		mergeSort(a, tmp,  0,  a.length - 1); 
	} 
	private static void mergeSort(Comparable [ ] a, Comparable [ ] tmp, int left, int right) //merge sort 
	{ 
		if( left < right ) 
		{ 
			int center = (left + right) / 2; 
			mergeSort(a, tmp, left, center); 
			mergeSort(a, tmp, center + 1, right); 
			merge(a, tmp, left, center + 1, right); 
		} 
	} 
	private static void merge(Comparable[ ] a, Comparable[ ] tmp, int left, int right, int rightEnd ) 
	{ 
		int leftEnd = right - 1; 
		int k = left; 
		int num = rightEnd - left + 1; 

		while(left <= leftEnd && right <= rightEnd) 
			if(a[left].compareTo(a[right]) <= 0) 
				tmp[k++] = a[left++]; 
			else 
				tmp[k++] = a[right++]; 

		while(left <= leftEnd)    // Copy rest of first half 
			tmp[k++] = a[left++]; 

		while(right <= rightEnd)  // Copy rest of right half 
			tmp[k++] = a[right++]; 

		// Copy tmp back 
		for(int i = 0; i < num; i++, rightEnd--) 
			a[rightEnd] = tmp[rightEnd]; 
	} 

	//method to check if a point is within a quad
	public static Boolean pointIn(Point2D compPoint, Point2D points[][]){
		boolean b = false;
		for(int i=0; i<points.length; i++){
			for(int j=0; j<points[i].length;j++){
				int k=j+1;
				if(k==points[i].length){
					k = 0;
				}
				if(points[i][j].getY() < compPoint.getY() && points[i][k].getY() >= compPoint.getY() || points[i][k].getY() < compPoint.getY() && points[i][j].getY() >= compPoint.getY()){
					if(points[i][j].getX()+(compPoint.getY()-points[i][j].getY())/(points[i][k].getY()-points[i][j].getY())*(points[i][k].getX()-points[i][j].getX())<compPoint.getX()){
						b=!b;
					}
				}

			}
		}
		return b;
	}
	//method to preprocess data 
	public static Polygon2D PreProcess(Polygon2D polygon){
		Point2D[] points = new Point2D[1]; 
		points = polygon.asPointsArray();
		//declare points
		double maxX = points[0].getX();
		double maxY = points[0].getY();
		double minX = points[0].getX();
		double minY = points[0].getY();
		Point2D maxXp = points[0];
		Point2D maxYp = points[0];
		Point2D minXp = points[0];
		Point2D minYp = points[0];

		//check if there is a higher/lower point
		for (int i = 1; i<points.length; i++) {
			if (points[i].getX() > maxX) {
				maxXp = points[i];
			}
			if (points[i].getY() > maxY) {
				maxYp = points[i];
			}
			if (points[i].getX() < minX) {
				minXp = points[i];
			}
			if (points[i].getY() < minY) {
				minYp = points[i];
			}
		}
		//create quad with points
		Point2D[][] quad = new Point2D[2][2];
		quad[1][1] = maxXp;
		quad[0][1] = maxYp;
		quad[1][0] = minXp;
		quad[0][0] = minYp;

		//check if any points are within quad
		List<Point2D> p = new ArrayList<Point2D>();
		for(int i=0; i<points.length; i++){
			if(!pointIn(points[i], quad)){
				p.add(points[i]);
			}
		}
		if(!p.contains(minXp)){
			p.add(maxXp);
		}
		if(!p.contains(minXp)){
			p.add(maxYp);
		}
		if(!p.contains(minXp)){
			p.add(minXp);
		}
		if(!p.contains(minXp)){
			p.add(minYp);
		}
		//convert to polygon and return
		Point2D[] newPoints = new Point2D[p.size()];
		newPoints = p.toArray(newPoints);
		polygon = new Polygon2D(newPoints); 

		return polygon;
	}

	public static Polygon2D findConvexHull(Polygon2D polygon) { 
		Point2D[] points = new Point2D[1]; 
		points = polygon.asPointsArray(); 
		Point2D lowest = lowestPoint(points); //get lowest hull point
		Vector[] vecs = new Vector[points.length]; 
		for(int i=0; i<points.length; i++){ 
			vecs[i] = new Vector(lowest, points[i]); 
		} 

		//sort by polar angle
		mergeSort(vecs); 

		StackNode<Point2D> hull = new StackNode<Point2D>(); //create hull stack
		hull.push(vecs[0].getPoint()); //add two initial points to hull
		hull.push(vecs[1].getPoint()); 
		for(int i=2; i<points.length; i++){ 
			while(Point2D.turningDirection(hull.sneeky_peek(), hull.peek(), vecs[i].getPoint()) == -1){//check if right/left turn 
				hull.pop(); //pop from stack
			} 
			hull.push(vecs[i].getPoint()); //push onto stack 
		} 
		int size = hull.size(); 
		Point2D[] hullPoints = new Point2D[size]; 
		for (int i=0; i<size; i++){ 
			hullPoints[i] = hull.pop(); 
		} 

		Vector[] testArray = new Vector[hullPoints.length]; 
		for(int i=0; i<hullPoints.length; i++){ 
			testArray[i] = new Vector(hullPoints[i], hullPoints[(i+1)%(hullPoints.length)]); 
			//StdDraw.line(testArray[i].getP0().getX(), testArray[i].getP0().getY(), testArray[i].getP1().getX(), testArray[i].getP1().getY()); 
		} 
		StdDraw.setPenColor(Color.RED); 

		Point2D[] test = Vector.removeColinear(testArray); //remove collinear points

		Point2D[] h = new Point2D[test.length]; 

		for (int i=0; i<test.length; i++){ 
			h[i] = test[i]; 
			StdDraw.setPenColor(Color.BLACK); 
			StdDraw.filledCircle(h[i].getX(), h[i].getY(), 0.004); 
		} 
		//polygon = new Polygon2D(hullPoints); 
		polygon = new Polygon2D(test); 

		return polygon; 
	} 


	//method to get lowest hull point
	public static Point2D lowestPoint(Point2D[] points) { 
		Point2D lowest = points[0]; 
		for(int i=0; i<points.length-1;i++){ 
			if(points[i].getY()<=lowest.getY()) { 
				if(points[i].getY()==lowest.getY() && points[i].getX()<lowest.getX()) { 
					lowest = points[i]; 
				} 
				else if(points[i].getY()!=lowest.getY()){ 
					lowest = points[i]; 
				} 
			} 
		} 
		swapLowest(points, lowest); 
		return lowest; 
	} 

	//helper method for lowestPoints()
	public static void swapLowest(Point2D[] points, Point2D lowest){ 
		Point2D temp = new Point2D(0,0); 
		for(int i=0; i<points.length-1;i++){ 
			if(points[i] == lowest){ 
				temp = points[0]; 
				points[0] = lowest; 
				points[i] = temp; 
			} 
		} 

	} 

}