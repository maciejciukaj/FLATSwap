namespace FlatSwap.Models
{
    public class Station
    {
        public int Id { get; set; }

        public required string Name { get; set; }

        public required string Country { get; set; }

        public string? Description { get; set; }

        public ICollection<Transcription> Transcriptions { get; set; } = new List<Transcription>();
    }
}
