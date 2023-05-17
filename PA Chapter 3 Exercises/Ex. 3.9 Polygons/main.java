import java.awt.Color;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;


public class main {

	public static void main(String[] args) {
		Point2D Start = new Point2D(1, 19);
		Point2D Goal01 = new Point2D(34, 3);
		Point2D Goal02 = new Point2D(32, 13);

		List<Polygon2D> list = createList();

		ShapeMap map = new ShapeMap(list, Start, Goal01);
//		ShapeMap map = new ShapeMap(list, Start, Goal02);

		//change the variable map or goal01 to change the point 
		//to find the shortest path between two points
		showFrame(map);

	}

	public static List<Polygon2D> createList(){
		Point2D Start = new Point2D(1, 19);
		Point2D Goal01 = new Point2D(34, 3);
		Point2D Goal02 = new Point2D(32, 13);


		Point2D p01 = new Point2D(2, 6);
		Point2D p02 = new Point2D(8, 3);
		Point2D p03 = new Point2D(11, 7);
		Point2D p04 = new Point2D(9, 14);
		Point2D p05 = new Point2D(3, 13);

		Point2D p06 = new Point2D(0, 0);
		Point2D [] arr = new Point2D[5];
		arr[0] = p01;
		arr[1] = p02;
		arr[2] = p03;
		arr[3] = p04;
		arr[4] = p05;
		Polygon2D poly01 =  new Polygon2D(arr);
		Point2D D = p05;
		Point2D E = p01;
		Point2D F = p02;
		Point2D G = p03;
		Point2D H = p04;

		p01 = new Point2D(4, 16);
		p02 = new Point2D(19, 16);
		p03 = new Point2D(19, 21);
		p04 = new Point2D(4, 21);
		arr = new Point2D[4];
		arr[0] = p01;
		arr[1] = p02;
		arr[2] = p03;
		arr[3] = p04;
		Polygon2D poly02 =  new Polygon2D(arr);
		Point2D B = p04;
		Point2D C = p01;
		Point2D L = p02;
		Point2D M = p03;

		p01 = new Point2D(14, 7);
		p02 = new Point2D(16, 14);
		p03 = new Point2D(12, 14);
		arr = new Point2D[3];
		arr[0] = p01;
		arr[1] = p02;
		arr[2] = p03;
		Polygon2D poly03 =  new Polygon2D(arr);
		Point2D I = p03;
		Point2D J = p01;
		Point2D K = p02;

		p01 = new Point2D(16, 3);
		p02 = new Point2D(16, 9);
		p03 = new Point2D(22, 5);
		p04 = new Point2D(20, 2);
		arr = new Point2D[4];
		arr[0] = p01;
		arr[1] = p02;
		arr[2] = p03;
		arr[3] = p04;
		Polygon2D poly04 =  new Polygon2D(arr);
		Point2D Q = p02;
		Point2D R = p01;
		Point2D S = p04;
		Point2D T = p03;

		p01 = new Point2D(25, 16);
		p02 = new Point2D(20, 12);
		p03 = new Point2D(21, 19);
		arr = new Point2D[3];
		arr[0] = p01;
		arr[1] = p02;
		arr[2] = p03;
		Polygon2D poly05 =  new Polygon2D(arr);
		Point2D N = p03;
		Point2D O = p02;
		Point2D P = p01;

		p01 = new Point2D(24, 3);
		p02 = new Point2D(30, 3);
		p03 = new Point2D(30, 13);
		p04 = new Point2D(24, 13);
		arr = new Point2D[4];
		arr[0] = p01;
		arr[1] = p02;
		arr[2] = p03;
		arr[3] = p04;
		Polygon2D poly06 =  new Polygon2D(arr);
		Point2D U = p01;
		Point2D V = p02;
		Point2D X = p04;
		Point2D Y = p03;

		p01 = new Point2D(33, 3);
		p02 = new Point2D(35, 6);
		p03 = new Point2D(34, 14);
		p04 = new Point2D(31, 5);
		arr = new Point2D[4];
		arr[0] = p01;
		arr[1] = p02;
		arr[2] = p03;
		arr[3] = p04;
		Polygon2D poly07 =  new Polygon2D(arr);
		Point2D E1 = p03;
		Point2D F1 = p04;
		Point2D G1 = p02;
		Point2D H1 = p01;

		p01 = new Point2D(31, 14);
		p02 = new Point2D(27, 16);
		p03 = new Point2D(27, 20);
		p04 = new Point2D(30, 21);
		p05 = new Point2D(33, 20);
		p06 = new Point2D(33, 16);
		arr = new Point2D[6];
		arr[0] = p01;
		arr[1] = p02;
		arr[2] = p03;
		arr[3] = p04;
		arr[4] = p05;
		arr[5] = p06;
		Polygon2D poly08 = new Polygon2D(arr);



		List<Polygon2D> listPoly = new ArrayList<Polygon2D>(8);
		listPoly.add(poly01);
		listPoly.add(poly02);
		listPoly.add(poly03); 
		listPoly.add(poly04); 
		listPoly.add(poly05);
		listPoly.add(poly06); 
		listPoly.add(poly07); 
		listPoly.add(poly08);


		return listPoly;
	}

	public static void showFrame(ShapeMap map) {
		//define canvas
		
		StdDraw.setTitle("Find the shortest path between start and goal points. (RED = Start, GREEN = Goal)");
		StdDraw.setCanvasSize(800, 400);
		StdDraw.setPenRadius(0.005);
		StdDraw.setXscale(0, 36);
		StdDraw.setYscale(0, 22);


		//start execution timer
		long startTime = System.currentTimeMillis();
//		System.out.println("");


		int hulls = 0;

		//array of point2d arrays of polygons 
		Point2D[][] convexHulls = new Point2D[map.amountofPolys()][];

		//find convex hull of every polygon on the map
		for (Polygon2D poly : map) {
			Polygon2D polygon = new Polygon2D(GrahamScan.findConvexHull(poly));
			Point2D points[] = polygon.asPointsArray();
			poly = GrahamScan.PreProcess(poly);
			StdDraw.setPenColor(Color.MAGENTA);
			poly.draw(); //draw polygons
			StdDraw.setPenColor(Color.BLUE);
			polygon.drawFilled(); //draw convex hulls
			//			StdDraw.setPenColor(Color.GRAY);
			//			poly.drawFilled();
			convexHulls[hulls] = points;
			//			StdDraw.setPenColor(Color.RED);
			//			poly.draw();
			hulls++;
		}

		//set start and end points
		Point2D startingPoint = map.sourcePoint();
		Point2D endPoint = map.destinationPoint();

		//generate paths in visibility graph
		List<Graph.Edge> paths = new ArrayList<Graph.Edge>();
		paths = VisibilityGraph.generatePaths(convexHulls, startingPoint, endPoint);

		//convert list to array
		Graph.Edge[] graph = new Graph.Edge[paths.size()];
		graph = paths.toArray(graph);

		//run best first search on graph
		Graph g = new Graph(graph);		
		g.uniformCost(startingPoint);
		System.out.println("RED = Start, GREEN = Goal");
		
		System.out.println("S ==>");
		g.printPath(endPoint);
		System.out.println("==> G");
		System.out.println();
		System.out.println();


		//get the optimal route as a list
		List<Point2D> route = new ArrayList<Point2D>();
		route = g.getPath();


		//indicate start and end points
		StdDraw.setPenColor(Color.BLACK);
		StdDraw.filledCircle(startingPoint.getX(), startingPoint.getY(), 0.004);
		StdDraw.filledCircle(endPoint.getX(), endPoint.getY(), 0.004);
		StdDraw.setPenColor(Color.RED);
		StdDraw.setPenRadius(0.05);
		startingPoint.draw();
		StdDraw.setPenColor(Color.GREEN);
		endPoint.draw();

		//				StdDraw.setPenColor(Color.MAGENTA);
		//				Goal02.draw();


		double totalDist = 0;

		//draw shortest path
		StdDraw.setPenColor(Color.RED);
		StdDraw.setPenRadius(0.010);
		for(int i=1; i<route.size();i++){
			StdDraw.line(route.get(i-1).getX(), route.get(i-1).getY(), route.get(i).getX(), route.get(i).getY());
			totalDist += VisibilityGraph.dist(route.get(i-1), route.get(i));
		}

		//display execution time
		long endTime   = System.currentTimeMillis();
		long totalTime = endTime - startTime;
		System.out.println("Execution time (ms) = " + totalTime);
		System.out.println("Length of path found = " + totalDist);

	}

}

class ShapeMap implements Iterable<Polygon2D> {

	private Point2D start_point;   // source point on map
	private Point2D end_point;  // destination point on map
	private ArrayList<Polygon2D> poly;  // polygon data


	public ShapeMap(Point2D src, Point2D dest) {
		poly = new ArrayList<Polygon2D>();
		start_point = new Point2D(src);
		end_point = new Point2D(dest);
	}

	public ShapeMap(List<Polygon2D> pgs, Point2D src, Point2D dest) {
		// defensive copy
		poly = new ArrayList<Polygon2D>();
		for (int i=0; i<pgs.size(); i++) {
			poly.add( new Polygon2D(pgs.get(i)) );
		}
		start_point = new Point2D(src);
		end_point = new Point2D(dest);
	}

	public void addPolygon(Polygon2D pg) {
		poly.add(pg);
	}

	public int amountofPolys() {
		return poly.size();
	}

	public void addPolygon(Point2D[] points) {
		Polygon2D pg = new Polygon2D();
		for (int i=0; i<points.length; i++) {
			pg.addPoint(points[i]);
		}
		addPolygon(pg);
	}

	public Point2D sourcePoint() {
		return start_point;
	}

	public Point2D destinationPoint () {
		return end_point;
	}

	@Override
	public Iterator<Polygon2D> iterator() {
		Iterator<Polygon2D> it = new Iterator<Polygon2D>() {
			private int currentIndex = 0;
			@Override
			public boolean hasNext() { return (currentIndex < poly.size()); }
			@Override
			public Polygon2D next() { return poly.get(currentIndex++); }
			@Override
			public void remove() { throw new UnsupportedOperationException(); }
		};
		return it;
	}

	public void draw() {
		for (int i=0; i<poly.size(); i++) {
			poly.get(i).draw();
		}
	}

	public void drawFilled() {
		for (int i=0; i<poly.size(); i++) {
			poly.get(i).drawFilled();
		}
	}

}


