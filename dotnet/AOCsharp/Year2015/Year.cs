using AOCSolutions;

namespace AOCsharp.Year2015;

public class Year : IYear
{
    public IDay GetDay(int day)
    {
        return day switch
        {
            1 => new Day1.Day(),
            _ => throw new InvalidDayException(day),
        };
    }
}
