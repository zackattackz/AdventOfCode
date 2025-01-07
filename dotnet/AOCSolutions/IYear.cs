namespace AOCSolutions;

public interface IYear
{
    public IDay GetDay(int day);
}

public class InvalidDayException (int day) : Exception(_getExceptionString(day))
{
    private static string _getExceptionString(int day) => $"Invalid day: {day}";
}
