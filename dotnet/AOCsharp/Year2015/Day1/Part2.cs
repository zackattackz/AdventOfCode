using AOCSolutions;

namespace AOCsharp.Year2015.Day1;

public class Part2 : IPart
{
    public string GetSolution(TextReader input)
    {
        var pos = 1;
        var floor = 0;
        foreach (var direction in Direction.ParseInput(input))
        {
            floor += Direction.GetFloorDelta(direction);
            if (floor == -1)
            {
                return pos.ToString();
            }
            pos++;
        }
        throw new Exception("Never entered basement");
    }
}
