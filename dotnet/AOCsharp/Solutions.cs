using AOCSolutions;

namespace AOCsharp;

public class Solutions : ISolutions
{
    public const string Name = "csharp";
    public string Solve(int yearInt, int dayInt, int partInt, TextReader input)
    {
        var year = GetYear(yearInt);
        var day = year.GetDay(dayInt);
        var part = day.GetPart(partInt);
        return part.GetSolution(input);
    }

    public IYear GetYear(int year)
    {
        return year switch
        {
            2015 => new Year2015.Year(),
            _ => throw new InvalidYearException(year),
        };
    }
}

public class InvalidYearException (int year) : Exception(_getExceptionString(year))
{
    private static string _getExceptionString(int year) => $"Invalid year: {year}";
}
