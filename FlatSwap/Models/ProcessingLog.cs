namespace FlatSwap.Models
{
    public class ProcessingLog
    {
        public int Id { get; set; }

        public int AudioFileId { get; set; }

        public required string Status { get; set; }

        public string? Details { get; set; }

        public DateTime Timestamp { get; set; } = DateTime.UtcNow;

        public required AudioFile AudioFile { get; set; }
    }
}
