namespace AOCsharp.Year2015.Day2;

public class Present
{
    public int Length { get; set; }

    public int Width { get; set; }

    public int Height { get; set; }

    public int SurfaceArea()
    {
        return 2 * Length * Width + 2 * Width * Height + 2 * Height * Length;
    }

    public (int,int)[] Sides()
    {
        return
        [
            (Length, Width),
            (Length, Height),
            (Width, Height)
        ];
    }

    public int MinSide()
    {
        return Sides().Select(sides => sides.Item1 * sides.Item2).Min();
    }

    public int RequiredPaperArea()
    {
        return SurfaceArea() + MinSide();
    }

    public int Volume()
    {
        return Length * Width * Height;
    }

    public int[] Perimeters()
    {
        return
        [
            Length * 2 + Width * 2,
            Height * 2 + Width * 2,
            Length * 2 + Height * 2,
        ];
    }

    public int MinPerimeter()
    {
        return Perimeters().Min();
    }

    public int RequiredRibbonLength()
    {
        return Volume() + MinPerimeter();
    }
}

public static class Parser
{
    public static IEnumerable<Present> ParseInput(TextReader input)
    {
        string? line;
        while ((line = input.ReadLine()) is not null)
        {
            var parts = line.Split("x");
            var present = new Present();
            if (parts.Length != 3
                || !int.TryParse(parts[0], out var length)
                || !int.TryParse(parts[1], out var width)
                || !int.TryParse(parts[2], out var height))
            {
                throw new Exception($"Invalid present input: {line}");
            }
            present.Length = length;
            present.Width = width;
            present.Height = height;
            yield return present;
        }
    }
}
