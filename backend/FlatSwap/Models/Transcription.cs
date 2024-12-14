using static System.Collections.Specialized.BitVector32;

namespace FlatSwap.Models
{
    public class Transcription
    {
        public int Id { get; set; }

        public required string TranscribedText { get; set; }

        public required string Frequency { get; set; }

        public DateTime Timestamp { get; set; } = DateTime.UtcNow;

        public int StationId { get; set; }

        public required Station Station { get; set; }
    }
}
