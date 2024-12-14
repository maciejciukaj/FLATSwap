using FlatSwap.Models;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System.Reflection.Emit;

namespace FlatSwap.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

        public DbSet<Transcription> Transcriptions { get; set; }
        public DbSet<Station> Stations { get; set; }
        public DbSet<AudioFile> AudioFiles { get; set; }
        public DbSet<ProcessingLog> ProcessingLogs { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<Station>()
                .HasMany(s => s.Transcriptions)
                .WithOne(t => t.Station)
                .HasForeignKey(t => t.StationId)
                .OnDelete(DeleteBehavior.Cascade);

            modelBuilder.Entity<ProcessingLog>()
                .HasOne(p => p.AudioFile)
                .WithMany()
                .HasForeignKey(p => p.AudioFileId);
        }
    }
}
