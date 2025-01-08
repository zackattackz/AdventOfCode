using AOCSolutions;

namespace AOCsharp.Year2015.Day1;

public class Part1 : IPart
{
    public string GetSolution(TextReader input)
    {
        var floor = Direction.ParseInput(input).Sum(Direction.GetFloorDelta);
        return floor.ToString();
    }
}
