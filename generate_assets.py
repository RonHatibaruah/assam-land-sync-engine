import os
import sys

# Ensure clean writable matplotlib directory
os.environ['MPLCONFIGDIR'] = '/tmp/matplotlib'
os.makedirs('/tmp/matplotlib', exist_ok=True)
os.makedirs('assets', exist_ok=True)

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Set consistent typography and styling
plt.rcParams['font.sans-serif'] = 'Helvetica, Arial, DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CCCCCC'
plt.rcParams['axes.linewidth'] = 0.8

def create_budget_chart():
    labels = [
        'Technical Engineering\nTeam (4 Specialists)\n₹20.0 L (50.0%)',
        'Cloud Infrastructure &\nStaging Sandbox\n₹5.0 L (12.5%)',
        'Field Pilot & Circle\nCapacity Building\n₹4.5 L (11.3%)',
        'Synthetic Testbed &\nGIS Tooling\n₹4.5 L (11.3%)',
        'Cert-IN Security Audit\n& VAPT\n₹3.5 L (8.8%)',
        'Operations, Travel &\nContingency\n₹2.5 L (6.3%)'
    ]
    sizes = [20.0, 5.0, 4.5, 4.5, 3.5, 2.5]
    colors = ['#1B365D', '#0A7E8C', '#2E7D32', '#F59E0B', '#8B5CF6', '#64748B']
    explode = (0.05, 0, 0, 0, 0, 0)

    fig, ax = plt.subplots(figsize=(8, 4.5), subplot_kw=dict(aspect="equal"))
    wedges, texts, autotexts = ax.pie(
        sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        startangle=140, colors=colors,
        textprops=dict(color="#1E293B", fontsize=9, fontweight='medium'),
        pctdistance=0.8,
        wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2)
    )
    for at in autotexts:
        at.set_color('white')
        at.set_fontsize(8)
        at.set_fontweight('bold')
    
    ax.set_title("Indicative Resource & Grant Budget Allocation (Total: ₹40.0 Lakhs)",
                 fontsize=12, fontweight='bold', color='#1B365D', pad=15)
    plt.tight_layout()
    plt.savefig('assets/budget_breakdown.png', dpi=300)
    plt.close()
    print("Created assets/budget_breakdown.png")

def create_latency_benchmark_chart():
    fig, ax = plt.subplots(figsize=(8, 3.8))
    
    metrics = ['Pre-Commit\nDag Lock', 'Dharitree\nJamabandi Upd', 'Bhunaksha\nVector Split', 'NGDRS\nEncumbrance Upd', 'Total Atomic\nSaga Commit']
    latencies_ms = [45, 120, 165, 90, 420]
    std_dev = [5, 15, 20, 10, 35]
    
    bars = ax.bar(metrics, latencies_ms, yerr=std_dev, capsize=5, color=['#0A7E8C', '#1B365D', '#2E7D32', '#6366F1', '#D97706'],
                  edgecolor='#333333', linewidth=0.8, alpha=0.9, width=0.55)
    
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)} ms',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 6),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold', color='#1E293B')
                    
    ax.axhline(2000, color='#EF4444', linestyle='--', linewidth=1.2, label='Target SLA Limit (< 2000 ms)')
    
    ax.set_ylabel('Execution Latency (Milliseconds)', fontsize=10, fontweight='bold', color='#1B365D')
    ax.set_title('BhumiSync Prototype Latency Benchmarks (Multi-System Synchronization)', fontsize=11, fontweight='bold', color='#1B365D', pad=12)
    ax.set_ylim(0, 700)
    ax.grid(axis='y', linestyle=':', alpha=0.6)
    ax.legend(loc='upper right', frameon=True, fontsize=9)
    
    plt.tight_layout()
    plt.savefig('assets/sync_latency_benchmark.png', dpi=300)
    plt.close()
    print("Created assets/sync_latency_benchmark.png")

def create_gantt_chart():
    fig, ax = plt.subplots(figsize=(9, 4.0))
    
    tasks = [
        "M1: Discovery & Architecture Spec",
        "M2: Kafka Event Mesh & PostGIS Alpha",
        "M3: End-to-End Staging MVP & Cockpits",
        "M4: Third-Party Cert-IN VAPT Audit",
        "M5: Field Pilot (2 Revenue Circles)",
        "M6: Evaluation, Handover & Scale Blueprint"
    ]
    starts = [0, 1.5, 3.5, 5.5, 6.5, 8.0]
    durations = [2.0, 2.5, 2.5, 1.5, 2.0, 1.0]
    colors = ['#1B365D', '#0A7E8C', '#2E7D32', '#D97706', '#6366F1', '#475569']
    
    y_pos = np.arange(len(tasks))
    ax.barh(y_pos, durations, left=starts, height=0.45, align='center', color=colors, edgecolor='#333333', linewidth=0.8)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(tasks, fontsize=9, fontweight='medium', color='#1E293B')
    ax.invert_yaxis()
    ax.set_xlabel('Project Timeline (Months)', fontsize=10, fontweight='bold', color='#1B365D')
    ax.set_title('BhumiSync 9-Month Phased Implementation Roadmap & Milestones', fontsize=11, fontweight='bold', color='#1B365D', pad=12)
    ax.set_xticks(range(0, 11))
    ax.set_xticklabels([f'M{i}' for i in range(0, 11)], fontsize=9)
    ax.grid(axis='x', linestyle=':', alpha=0.6)
    
    # Validation Ready Line
    ax.axvline(6.0, color='#DC2626', linestyle='--', linewidth=1.5, label='MVP Ready for Staging Validation (M6)')
    ax.axvline(8.5, color='#16A34A', linestyle='--', linewidth=1.5, label='Pilot Sign-Off (M8.5)')
    ax.legend(loc='lower right', frameon=True, fontsize=8)
    
    plt.tight_layout()
    plt.savefig('assets/gantt_timeline.png', dpi=300)
    plt.close()
    print("Created assets/gantt_timeline.png")

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Background Canvas Box
    ax.add_patch(patches.Rectangle((1, 1), 98, 98, fill=True, color='#F8FAFC', ec='#CBD5E1', lw=1))
    
    # Top Pillar Boxes: Source Systems
    # 1. NGDRS
    ax.add_patch(patches.FancyBboxPatch((4, 68), 26, 24, boxstyle="round,pad=1", fc="#EFF6FF", ec="#3B82F6", lw=1.5))
    ax.text(17, 86, "NGDRS / e-Panjeeyan", ha="center", va="center", fontsize=10, fontweight="bold", color="#1D4ED8")
    ax.text(17, 78, "• SRO Deed Execution\n• Stamp Duty & Fees\n• Buyer/Seller Party KYC", ha="center", va="center", fontsize=8, color="#334155")
    ax.text(17, 70, "[CDC Agent: Debezium]", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#2563EB")
    
    # 2. Dharitree
    ax.add_patch(patches.FancyBboxPatch((37, 68), 26, 24, boxstyle="round,pad=1", fc="#F0FDF4", ec="#22C55E", lw=1.5))
    ax.text(50, 86, "Dharitree (ILRMS)", ha="center", va="center", fontsize=10, fontweight="bold", color="#15803D")
    ax.text(50, 78, "• RoR & Jamabandi\n• Chitha Registers\n• Mutation / Namjari", ha="center", va="center", fontsize=8, color="#334155")
    ax.text(50, 70, "[CDC Agent: Debezium]", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#16A34A")

    # 3. Bhunaksha
    ax.add_patch(patches.FancyBboxPatch((70, 68), 26, 24, boxstyle="round,pad=1", fc="#FEF3C7", ec="#F59E0B", lw=1.5))
    ax.text(83, 86, "Bhunaksha (GIS)", ha="center", va="center", fontsize=10, fontweight="bold", color="#B45309")
    ax.text(83, 78, "• Cadastral Map Vectors\n• Dag Boundaries\n• WFS-T Map Services", ha="center", va="center", fontsize=8, color="#334155")
    ax.text(83, 70, "[Spatial WFS-T / Topo]", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#D97706")

    # Middle Layer: BhumiSync Core Integration Middleware
    ax.add_patch(patches.FancyBboxPatch((4, 25), 92, 34, boxstyle="round,pad=1", fc="#1E293B", ec="#0F172A", lw=2))
    ax.text(50, 54, "BHUMISYNC CORE ENTERPRISE SYNCHRONIZATION ENGINE", ha="center", va="center", fontsize=10.5, fontweight="bold", color="#F8FAFC")
    
    # Components inside BhumiSync
    # Event Mesh
    ax.add_patch(patches.FancyBboxPatch((7, 30), 25, 18, boxstyle="round,pad=0.5", fc="#334155", ec="#64748B", lw=1))
    ax.text(19.5, 43, "Apache Kafka / CDC", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#38BDF8")
    ax.text(19.5, 36, "Event Mesh & Ingestion\nSub-second streaming", ha="center", va="center", fontsize=7.5, color="#E2E8F0")

    # Saga Orchestrator
    ax.add_patch(patches.FancyBboxPatch((35, 30), 29, 18, boxstyle="round,pad=0.5", fc="#334155", ec="#64748B", lw=1))
    ax.text(49.5, 43, "Saga Transaction SEC", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#4ADE80")
    ax.text(49.5, 36, "Distributed State Machine\nTwo-Phase Commit & Rollback", ha="center", va="center", fontsize=7.5, color="#E2E8F0")

    # GeoSync Engine
    ax.add_patch(patches.FancyBboxPatch((67, 30), 26, 18, boxstyle="round,pad=0.5", fc="#334155", ec="#64748B", lw=1))
    ax.text(80, 43, "GeoSync PostGIS", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#FBBF24")
    ax.text(80, 36, "Cadastral Topology Check\nEuler-Poincaré & Dag Split", ha="center", va="center", fontsize=7.5, color="#E2E8F0")

    # Bottom Layer: Security, Audit & Stakeholder Dashboards
    ax.add_patch(patches.FancyBboxPatch((4, 4), 44, 16, boxstyle="round,pad=1", fc="#F1F5F9", ec="#94A3B8", lw=1.2))
    ax.text(26, 15, "Security & Audit Governance", ha="center", va="center", fontsize=9, fontweight="bold", color="#0F172A")
    ax.text(26, 9, "• Immutable Cryptographic Audit Log\n• Keycloak OIDC/RBAC & e-Sign/DSC PKI", ha="center", va="center", fontsize=7.5, color="#334155")

    ax.add_patch(patches.FancyBboxPatch((52, 4), 44, 16, boxstyle="round,pad=1", fc="#F1F5F9", ec="#94A3B8", lw=1.2))
    ax.text(74, 15, "Stakeholder Cockpit Interfaces", ha="center", va="center", fontsize=9, fontweight="bold", color="#0F172A")
    ax.text(74, 9, "• Circle Officer Unified Approval Cockpit\n• Lat Mandal Mobile Tool & Citizen e-Khaitan", ha="center", va="center", fontsize=7.5, color="#334155")

    # Connecting Arrows
    ax.annotate('', xy=(17, 61), xytext=(17, 68), arrowprops=dict(arrowstyle="<->", color="#3B82F6", lw=1.5))
    ax.annotate('', xy=(50, 61), xytext=(50, 68), arrowprops=dict(arrowstyle="<->", color="#22C55E", lw=1.5))
    ax.annotate('', xy=(83, 61), xytext=(83, 68), arrowprops=dict(arrowstyle="<->", color="#F59E0B", lw=1.5))
    
    ax.annotate('', xy=(26, 21), xytext=(26, 25), arrowprops=dict(arrowstyle="<->", color="#64748B", lw=1.2))
    ax.annotate('', xy=(74, 21), xytext=(74, 25), arrowprops=dict(arrowstyle="<->", color="#64748B", lw=1.2))

    plt.tight_layout()
    plt.savefig('assets/arch_diagram.png', dpi=300)
    plt.close()
    print("Created assets/arch_diagram.png")

def create_wireframe_mockup():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.8))
    
    # Panel 1: Circle Officer Cockpit Wireframe
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.add_patch(patches.Rectangle((0, 0), 100, 100, fc="#FFFFFF", ec="#1E293B", lw=1.5))
    ax1.add_patch(patches.Rectangle((0, 88), 100, 12, fc="#1B365D", ec="#1B365D"))
    ax1.text(50, 94, "Circle Officer Unified Cockpit - Case #ASM-DIS-2026-884", ha="center", va="center", color="white", fontsize=8.5, fontweight="bold")
    
    # Left Sub-panel: Jamabandi Diff
    ax1.add_patch(patches.Rectangle((3, 40), 45, 45, fc="#F8FAFC", ec="#CBD5E1", lw=1))
    ax1.text(25.5, 80, "Textual Jamabandi (Dharitree)", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#1E293B")
    ax1.text(25.5, 60, "Patta: 142 (Kheraj)\nDag: 588 -> Split [588/1, 588/2]\nPattadar Pre: Bipin Sarma (100%)\nPattadar Post:\n• B. Sarma: 1.5 Bigha (588/1)\n• R. Kalita: 1.0 Bigha (588/2)", ha="center", va="center", fontsize=6.8, color="#334155")
    
    # Right Sub-panel: Cadastral Vector Diff
    ax1.add_patch(patches.Rectangle((52, 40), 45, 45, fc="#F8FAFC", ec="#CBD5E1", lw=1))
    ax1.text(74.5, 80, "Cadastral Topology (Bhunaksha)", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#1E293B")
    
    # Simulated polygon split
    ax1.add_patch(patches.Polygon([[56, 45], [56, 72], [73, 72], [73, 45]], closed=True, fc="#BBF7D0", ec="#16A34A", lw=1.2))
    ax1.text(64.5, 58, "Dag 588/1\n1.50 B", ha="center", va="center", fontsize=6.5, fontweight="bold", color="#15803D")
    
    ax1.add_patch(patches.Polygon([[73, 45], [73, 72], [92, 72], [92, 45]], closed=True, fc="#BAE6FD", ec="#0284C7", lw=1.2))
    ax1.text(82.5, 58, "Dag 588/2\n1.00 B", ha="center", va="center", fontsize=6.5, fontweight="bold", color="#0369A1")
    
    # Bottom Verification Bar
    ax1.add_patch(patches.Rectangle((3, 18), 94, 18, fc="#F0FDF4", ec="#86EFAC", lw=1))
    ax1.text(50, 29, "✓ Boundary Invariant Verified (Euler-Poincaré Pass)\n✓ Zero Area Discrepancy (Δ = 0.00 sq m) | ✓ SRO Deed Verified", ha="center", va="center", fontsize=6.5, color="#166534")
    
    # Action Buttons
    ax1.add_patch(patches.Rectangle((20, 4), 28, 10, fc="#10B981", ec="#059669", lw=1))
    ax1.text(34, 9, "Approve & e-Sign", ha="center", va="center", color="white", fontsize=7.5, fontweight="bold")
    ax1.add_patch(patches.Rectangle((52, 4), 28, 10, fc="#EF4444", ec="#DC2626", lw=1))
    ax1.text(66, 9, "Reject / Query", ha="center", va="center", color="white", fontsize=7.5, fontweight="bold")

    # Panel 2: Lat Mandal Mobile Assistant Wireframe
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.add_patch(patches.Rectangle((0, 0), 100, 100, fc="#FFFFFF", ec="#1E293B", lw=1.5))
    ax2.add_patch(patches.Rectangle((0, 88), 100, 12, fc="#0A7E8C", ec="#0A7E8C"))
    ax2.text(50, 94, "Lat Mandal Field GIS Tool (Offline-Capable)", ha="center", va="center", color="white", fontsize=8.5, fontweight="bold")
    
    # Map Canvas
    ax2.add_patch(patches.Rectangle((5, 30), 90, 54, fc="#F1F5F9", ec="#94A3B8", lw=1))
    ax2.text(50, 78, "Survey Map View (GPS Accuracy ±0.05m)", ha="center", va="center", fontsize=7, color="#64748B")
    
    # Draw parcel with partition line
    ax2.add_patch(patches.Polygon([[18, 38], [18, 70], [80, 70], [80, 38]], closed=True, fc="#FEF9C3", ec="#CA8A04", lw=1.5))
    ax2.plot([48, 48], [38, 70], color="#DC2626", linestyle="--", linewidth=2, label="Split Line")
    ax2.plot([48], [54], 'ro', markersize=6)
    ax2.text(32, 54, "Point P1\n[26.184 N]", fontsize=6, ha="center", color="#854D0E")
    ax2.text(64, 54, "Point P2\n[91.751 E]", fontsize=6, ha="center", color="#854D0E")
    
    # Area Conservation Indicator
    ax2.add_patch(patches.Rectangle((5, 14), 90, 13, fc="#EFF6FF", ec="#BFDBFE", lw=1))
    ax2.text(50, 20.5, "Total Area: 2.50 Bigha | Sub-A: 1.50 B | Sub-B: 1.00 B\nArea Conserved: 100.0% (Tolerance: 0.00%)", ha="center", va="center", fontsize=6.8, fontweight="bold", color="#1E40AF")
    
    # Submit Button
    ax2.add_patch(patches.Rectangle((25, 3), 50, 8, fc="#0A7E8C", ec="#08636E", lw=1))
    ax2.text(50, 7, "Sync with Circle Office", ha="center", va="center", color="white", fontsize=7.5, fontweight="bold")

    plt.tight_layout()
    plt.savefig('assets/wireframe_dashboard.png', dpi=300)
    plt.close()
    print("Created assets/wireframe_dashboard.png")

if __name__ == '__main__':
    create_budget_chart()
    create_latency_benchmark_chart()
    create_gantt_chart()
    create_architecture_diagram()
    create_wireframe_mockup()
    print("All graphic assets successfully created!")
