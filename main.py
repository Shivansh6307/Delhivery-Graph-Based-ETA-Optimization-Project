"""
End-to-end pipeline runner.
Usage: python main.py
Runs, in order: data generation -> graph analysis -> ETA modeling ->
FTL/Carting classification -> strategy memo rendering.
"""
import os

from src import data_generator, graph_analysis, eta_model, ftl_carting, strategy_memo

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    print("Step 1/5: Generating synthetic trip data...")
    data_generator.generate()

    print("\nStep 2/5: Building network graph & bottleneck analysis...")
    graph_analysis.run()

    print("\nStep 3/5: Training baseline vs graph-enhanced ETA models...")
    eta_model.run()

    print("\nStep 4/5: Training FTL vs Carting routing classifier...")
    ftl_carting.run()

    print("\nStep 5/5: Rendering strategy memo...")
    strategy_memo.run()

    print("\n✅ Pipeline complete. See outputs/ for all charts and CSVs.")
