using AOCSolutions;

namespace AOCsharp.Year2015.Day3;

public class Part1 : IPart
{
    public string GetSolution(TextReader input)
    {
        int y = 0, x = 0;
        Dictionary<(int,int),int> coordVisits = new();
        coordVisits[(y,x)] = 1;
        foreach ((int dirY, int dirX) in Coords.Parse(input))
        {
            y += dirY;
            x += dirX;
            if(coordVisits.ContainsKey((y,x)))
            {
                coordVisits[(y,x)] += 1;
            } else
            {
                coordVisits[(y,x)] = 1;
            }
        }
        return coordVisits.Count.ToString();
    }
}

