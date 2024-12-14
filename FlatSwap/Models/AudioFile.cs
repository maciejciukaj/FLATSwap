namespace FlatSwap.Models
{
    public class AudioFile
    {
        public int Id { get; set; }

        public required string FileName { get; set; }

        public required string FilePath { get; set; }

        public DateTime RecordedAt { get; set; } = DateTime.UtcNow;

        public bool IsProcessed { get; set; } = false;
    }
}
