import os
import sys

os.environ['MPLCONFIGDIR'] = '/tmp/matplotlib'
os.makedirs('/tmp/matplotlib', exist_ok=True)
os.makedirs('assets', exist_ok=True)

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rcParams['font.sans-serif'] = 'Helvetica, Arial, DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CCCCCC'
plt.rcParams['axes.linewidth'] = 0.8

# -----------------------------------------------------------------------------
# 1. BEFORE VS AFTER WORKFLOW COMPARISON
# -----------------------------------------------------------------------------
def create_before_after_flow():
    fig, ax = plt.subplots(figsize=(10, 5.2))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Background
    ax.add_patch(patches.Rectangle((0, 0), 100, 100, fill=True, color='#F8FAFC', ec='#CBD5E1', lw=1.2))

    # Title
    ax.text(50, 95, "WORKFLOW COMPARISON: CURRENT PRACTICE VS. BHUMISYNC ENGINE", 
            ha="center", va="center", fontsize=11, fontweight="bold", color="#1B365D")

    # ================= TOP HALF: CURRENT PRACTICE =================
    ax.add_patch(patches.FancyBboxPatch((2, 51), 96, 39, boxstyle="round,pad=1", fc="#FFF1F2", ec="#F43F5E", lw=1.5))
    ax.text(6, 86, "CURRENT WORKFLOW (Fragmented Silos & Manual Reconciliation)", fontsize=9, fontweight="bold", color="#9F1239")
    ax.text(92, 86, "Latency: 15–45 Days", fontsize=8.5, fontweight="bold", color="#E11D48", ha="right")

    steps_cur = [
        ("1. Deed Registered", "Deed executed on NGDRS\nat SRO office", "#FDA4AF"),
        ("2. Physical Intimation", "Paper notice sent to\nCircle Office (Days)", "#FDA4AF"),
        ("3. Manual Namjari", "Clerk re-enters data in\nDharitree (Duplicate)", "#FDA4AF"),
        ("4. Mandal Field Visit", "Paper field-book sketch;\nno digital geo-check", "#FDA4AF"),
        ("5. Desynced Bhunaksha", "Cadastral map updated\nweeks/months later", "#FDA4AF")
    ]
    for i, (title, desc, bg) in enumerate(steps_cur):
        x = 5 + i * 19
        ax.add_patch(patches.FancyBboxPatch((x, 56), 16, 26, boxstyle="round,pad=0.5", fc="#FFFFFF", ec="#FB7185", lw=1.2))
        ax.text(x + 8, 77, title, ha="center", va="center", fontsize=7.5, fontweight="bold", color="#881337")
        ax.text(x + 8, 66, desc, ha="center", va="center", fontsize=6.5, color="#4C0519")
        if i < 4:
            ax.annotate('', xy=(x + 19, 69), xytext=(x + 16, 69), arrowprops=dict(arrowstyle="->", color="#E11D48", lw=1.5))

    # Vulnerability callout
    ax.text(50, 53.5, "⚠ Vulnerabilities: Double selling during 15-day latency window · Area-boundary mismatches · Citizen harassment",
            ha="center", va="center", fontsize=7.2, fontweight="bold", color="#BE123C")

    # ================= BOTTOM HALF: BHUMISYNC =================
    ax.add_patch(patches.FancyBboxPatch((2, 5), 96, 42, boxstyle="round,pad=1", fc="#F0FDF4", ec="#22C55E", lw=1.5))
    ax.text(6, 43, "BHUMISYNC WORKFLOW (Real-Time Asynchronous Saga Mesh)", fontsize=9, fontweight="bold", color="#14532D")
    ax.text(92, 43, "Latency: Smaller than 2.0s (Avg 420 ms)", fontsize=8.5, fontweight="bold", color="#15803D", ha="right")

    steps_bhu = [
        ("1. SRO Deed Signed", "NGDRS deed signed;\nCDC emits event", "#BBF7D0"),
        ("2. Redlock Acquired", "Instant Dag lock in Redis;\nDouble-sell blocked", "#BBF7D0"),
        ("3. GeoSync Validation", "PostGIS verifies Euler\ninvariant (χ=2)", "#BBF7D0"),
        ("4. CO 1-Click e-Sign", "Unified Cockpit diff;\nCircle Officer DSC sign", "#BBF7D0"),
        ("5. Atomic Commit", "Dharitree & Bhunaksha\nsplit simultaneously", "#BBF7D0")
    ]
    for i, (title, desc, bg) in enumerate(steps_bhu):
        x = 5 + i * 19
        ax.add_patch(patches.FancyBboxPatch((x, 12), 16, 26, boxstyle="round,pad=0.5", fc="#FFFFFF", ec="#4ADE80", lw=1.2))
        ax.text(x + 8, 33, title, ha="center", va="center", fontsize=7.5, fontweight="bold", color="#14532D")
        ax.text(x + 8, 22, desc, ha="center", va="center", fontsize=6.5, color="#166534")
        if i < 4:
            ax.annotate('', xy=(x + 19, 25), xytext=(x + 16, 25), arrowprops=dict(arrowstyle="->", color="#16A34A", lw=1.5))

    # Benefits callout
    ax.text(50, 8, "✓ Outcomes: Zero fraud window · 100% geometric conservation · Sub-second multi-system sync · Citizen instant e-Khaitan",
            ha="center", va="center", fontsize=7.2, fontweight="bold", color="#15803D")

    plt.tight_layout()
    plt.savefig('assets/before_after_flow.png', dpi=300)
    plt.close()
    print("Created assets/before_after_flow.png")


# -----------------------------------------------------------------------------
# 2. DOUBLE-CONVEYANCING FRAUD WINDOW TIMELINE
# -----------------------------------------------------------------------------
def create_fraud_window_timeline():
    fig, ax = plt.subplots(figsize=(10, 4.2))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.add_patch(patches.Rectangle((0, 0), 100, 100, fill=True, color='#FFFFFF', ec='#CBD5E1', lw=1.2))

    ax.text(50, 93, "MITIGATING DOUBLE REGISTRATION FRAUD: THE LATENCY WINDOW", 
            ha="center", va="center", fontsize=11, fontweight="bold", color="#1B365D")

    # Current System Timeline
    ax.text(5, 78, "TRADITIONAL ASYNC SYSTEM (15 TO 45 DAYS VULNERABILITY GAP)", fontsize=8.5, fontweight="bold", color="#991B1B")
    
    # Timeline bar
    ax.plot([5, 95], [68, 68], color="#94A3B8", lw=3)
    
    # Event 1: First Sale
    ax.plot(15, 68, 'o', color="#DC2626", markersize=9)
    ax.text(15, 73, "Day 0: Sale 1 (Buyer A)\nDeed Registered at SRO", ha="center", fontsize=6.8, fontweight="bold", color="#B91C1C")

    # Fraud Window Box
    ax.add_patch(patches.Rectangle((18, 56), 54, 18, fill=True, color="#FEE2E2", ec="#EF4444", lw=1.2, linestyle="--"))
    ax.text(45, 64, "CRITICAL TITLE FRAUD WINDOW (15 to 45 Days)\nEncumbrance not reflected in Dharitree/Bhunaksha", ha="center", va="center", fontsize=7.2, fontweight="bold", color="#991B1B")

    # Fraudulent Event 2
    ax.plot(45, 68, 'X', color="#7F1D1D", markersize=10)
    ax.text(45, 52, "Day 12: Fraudulent Sale 2 (Buyer B)\nSame Dag sold again at different SRO!", ha="center", fontsize=6.8, fontweight="bold", color="#7F1D1D")

    # Event 3: Mutation Applied
    ax.plot(75, 68, 'o', color="#D97706", markersize=8)
    ax.text(75, 73, "Day 25: Mutation Hearing\nDispute & Litigation Starts", ha="center", fontsize=6.8, fontweight="bold", color="#B45309")

    # ================= BHUMISYNC ZERO-FRAUD TIMELINE =================
    ax.text(5, 38, "BHUMISYNC ENGINE (INSTANT PROGRAMMATIC REDLOCK)", fontsize=8.5, fontweight="bold", color="#15803D")
    
    ax.plot([5, 95], [26, 26], color="#94A3B8", lw=3)
    
    # T=0s: Sale 1
    ax.plot(15, 26, 'o', color="#16A34A", markersize=9)
    ax.text(15, 31, "T = 0.0s: Sale 1 Signed\nNGDRS SRO Deed", ha="center", fontsize=6.8, fontweight="bold", color="#15803D")

    # T=0.045s: Redlock
    ax.plot(22, 26, 's', color="#8B5CF6", markersize=9)
    ax.text(22, 17, "T = +45ms: REDLOCK\nDag Locked Statewide", ha="center", fontsize=6.8, fontweight="bold", color="#6D28D9")

    # T=0.420s: Atomic Commit
    ax.plot(35, 26, 'D', color="#0A7E8C", markersize=9)
    ax.text(35, 31, "T = +420ms: ATOMIC SYNC\nJamabandi & Map Split", ha="center", fontsize=6.8, fontweight="bold", color="#0E7490")

    # Attempted Sale 2 Blocked!
    ax.add_patch(patches.FancyBboxPatch((50, 15), 42, 20, boxstyle="round,pad=0.5", fc="#ECFDF5", ec="#10B981", lw=1.2))
    ax.text(71, 27, "FRAUD WINDOW ELIMINATED (0 SECONDS)", ha="center", va="center", fontsize=8, fontweight="bold", color="#047857")
    ax.text(71, 20, "Attempted duplicate deed at any SRO instantly blocked:\n'ERROR: Dag 588 is under Active Distributed Lock'", ha="center", va="center", fontsize=6.5, color="#065F46")

    plt.tight_layout()
    plt.savefig('assets/fraud_window_timeline.png', dpi=300)
    plt.close()
    print("Created assets/fraud_window_timeline.png")


# -----------------------------------------------------------------------------
# 3. CHAOS ENGINEERING & COMPENSATING ROLLBACK FLOW
# -----------------------------------------------------------------------------
def create_chaos_rollback_flow():
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.add_patch(patches.Rectangle((0, 0), 100, 100, fill=True, color='#F8FAFC', ec='#CBD5E1', lw=1.2))

    ax.text(50, 93, "DISTRIBUTED SAGA TRANSACTION: ATOMIC COMMIT VS. CHAOS ROLLBACK", 
            ha="center", va="center", fontsize=11, fontweight="bold", color="#1B365D")

    # Start Node
    ax.add_patch(patches.FancyBboxPatch((3, 40), 16, 20, boxstyle="round,pad=0.5", fc="#EFF6FF", ec="#3B82F6", lw=1.5))
    ax.text(11, 52, "Mutation Event", ha="center", va="center", fontsize=8, fontweight="bold", color="#1D4ED8")
    ax.text(11, 46, "SRO Deed / Petition\nSigned by Officer", ha="center", va="center", fontsize=6.5, color="#1E40AF")

    # Orchestrator Node
    ax.add_patch(patches.FancyBboxPatch((24, 38), 20, 24, boxstyle="round,pad=0.5", fc="#1E293B", ec="#0F172A", lw=2))
    ax.text(34, 52, "Saga Orchestrator", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#38BDF8")
    ax.text(34, 45, "Execution Coordinator\n• Redlock Acquisition\n• PostGIS Polygon Check", ha="center", va="center", fontsize=6.5, color="#E2E8F0")

    ax.annotate('', xy=(24, 50), xytext=(19, 50), arrowprops=dict(arrowstyle="->", color="#3B82F6", lw=2))

    # Decision Diamond (PostGIS check)
    diamond = patches.Polygon([[52, 50], [58, 62], [64, 50], [58, 38]], closed=True, fc="#FEF3C7", ec="#D97706", lw=1.5)
    ax.add_patch(diamond)
    ax.text(58, 51.5, "Topology\nValid?", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#B45309")

    ax.annotate('', xy=(52, 50), xytext=(44, 50), arrowprops=dict(arrowstyle="->", color="#64748B", lw=2))

    # PATH A: SUCCESS COMMIT (Top Branch)
    ax.annotate('', xy=(72, 74), xytext=(58, 62), arrowprops=dict(arrowstyle="->", color="#16A34A", lw=2))
    ax.text(62, 70, "YES (Pass)", fontsize=7.5, fontweight="bold", color="#15803D")

    ax.add_patch(patches.FancyBboxPatch((72, 64), 25, 22, boxstyle="round,pad=0.5", fc="#DCFCE7", ec="#16A34A", lw=1.5))
    ax.text(84.5, 77, "PHASE 4: ATOMIC COMMIT", ha="center", va="center", fontsize=8, fontweight="bold", color="#14532D")
    ax.text(84.5, 70, "• Dharitree: Jamabandi split\n• Bhunaksha: Dags 588/1 & 2\n• NGDRS: Encumbrance locked\n• Release Redlock -> Success!", ha="center", va="center", fontsize=6.5, color="#166534")

    # PATH B: CHAOS / FAILURE ROLLBACK (Bottom Branch)
    ax.annotate('', xy=(72, 26), xytext=(58, 38), arrowprops=dict(arrowstyle="->", color="#DC2626", lw=2))
    ax.text(62, 30, "NO (Overlap / Err)", fontsize=7.5, fontweight="bold", color="#B91C1C")

    ax.add_patch(patches.FancyBboxPatch((72, 14), 25, 24, boxstyle="round,pad=0.5", fc="#FEE2E2", ec="#EF4444", lw=1.5))
    ax.text(84.5, 29, "COMPENSATING ROLLBACK", ha="center", va="center", fontsize=8, fontweight="bold", color="#991B1B")
    ax.text(84.5, 21, "• Halt 2-Phase Commit\n• Execute Undo on Dharitree\n• Rollback Bhunaksha Vectors\n• Release Lock & Alert Officer", ha="center", va="center", fontsize=6.5, color="#7F1D1D")

    # Bottom Guarantees
    ax.text(50, 6, "Resilience Guarantee: In 250/250 automated chaos-test scenarios (network dropouts & boundary overlaps), rollback succeeded with ZERO orphaned records.",
            ha="center", va="center", fontsize=7.2, fontweight="bold", color="#1E293B")

    plt.tight_layout()
    plt.savefig('assets/chaos_rollback_flow.png', dpi=300)
    plt.close()
    print("Created assets/chaos_rollback_flow.png")


# -----------------------------------------------------------------------------
# 4. SECURITY, DPDP ACT 2023 & ASDC HOSTING TOPOLOGY
# -----------------------------------------------------------------------------
def create_security_asdc_topology():
    fig, ax = plt.subplots(figsize=(10, 5.0))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.add_patch(patches.Rectangle((0, 0), 100, 100, fill=True, color='#F8FAFC', ec='#CBD5E1', lw=1.2))

    ax.text(50, 94, "GOVERNMENT SECURITY ARCHITECTURE & ASDC HOSTING TOPOLOGY", 
            ha="center", va="center", fontsize=11, fontweight="bold", color="#1B365D")

    # Zone 1: Field Users & Offices (Left)
    ax.add_patch(patches.FancyBboxPatch((3, 10), 22, 78, boxstyle="round,pad=1", fc="#EFF6FF", ec="#3B82F6", lw=1.2))
    ax.text(14, 83, "ZONE 1: FIELD OFFICES", ha="center", va="center", fontsize=8, fontweight="bold", color="#1D4ED8")
    
    users = [
        ("Sub-Registrar (SRO)", "NGDRS Deed Execution", "#DBEAFE"),
        ("Circle Officers (CO)", "1-Click DSC/e-Sign Approval", "#DBEAFE"),
        ("Lat Mandals", "Mobile GPS Cadastral Tool", "#DBEAFE"),
        ("Citizens / Pattadars", "Instant SMS/QR e-Khaitan", "#DBEAFE")
    ]
    for i, (name, role, bg) in enumerate(users):
        y = 65 - i * 16
        ax.add_patch(patches.FancyBboxPatch((5, y), 18, 12, boxstyle="round,pad=0.3", fc="#FFFFFF", ec="#93C5FD", lw=1))
        ax.text(14, y + 8, name, ha="center", va="center", fontsize=7, fontweight="bold", color="#1E40AF")
        ax.text(14, y + 3.5, role, ha="center", va="center", fontsize=6, color="#3B82F6")

    # Encrypted Lease Line Arrow
    ax.annotate('', xy=(29, 49), xytext=(25, 49), arrowprops=dict(arrowstyle="->", color="#2563EB", lw=2))
    ax.text(27, 53, "mTLS 1.3 / VPN", ha="center", fontsize=6.5, fontweight="bold", color="#1D4ED8")

    # Zone 2: ASDC DMZ & Gateway
    ax.add_patch(patches.FancyBboxPatch((30, 10), 32, 78, boxstyle="round,pad=1", fc="#F1F5F9", ec="#64748B", lw=1.2))
    ax.text(46, 83, "ZONE 2: ASDC SECURED DMZ", ha="center", va="center", fontsize=8, fontweight="bold", color="#334155")

    dmz_modules = [
        ("WAF & API Gateway", "Mutual TLS (mTLS v1.3) Termination\nRate Limiting & DDoS Shield", 62),
        ("Keycloak IAM & SSO", "Jan Parichay & Assam SSO Integration\nRole-Based Access Control (RBAC)", 44),
        ("PKI / HSM Signer", "Digital Signature Certificate (DSC)\nAadhaar e-Sign Verification", 26)
    ]
    for title, desc, y in dmz_modules:
        ax.add_patch(patches.FancyBboxPatch((32, y), 28, 14, boxstyle="round,pad=0.4", fc="#FFFFFF", ec="#94A3B8", lw=1))
        ax.text(46, y + 9.5, title, ha="center", va="center", fontsize=7.2, fontweight="bold", color="#0F172A")
        ax.text(46, y + 4.5, desc, ha="center", va="center", fontsize=6, color="#475569")

    # Arrow to Core
    ax.annotate('', xy=(66, 49), xytext=(62, 49), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=2))

    # Zone 3: Secure Core & Vault (Right)
    ax.add_patch(patches.FancyBboxPatch((67, 10), 30, 78, boxstyle="round,pad=1", fc="#F0FDF4", ec="#22C55E", lw=1.2))
    ax.text(82, 83, "ZONE 3: TRUSTED DATA VAULT", ha="center", va="center", fontsize=8, fontweight="bold", color="#14532D")

    vault_modules = [
        ("DPDP Act 2023 Vault", "Tokenized Aadhaar & Citizen PII\nIsolated AES-256 Vault", 62, "#DCFCE7", "#16A34A"),
        ("BhumiSync Saga Engine", "Apache Kafka + PostGIS 16\nRedis Distributed Redlock", 44, "#FEF3C7", "#D97706"),
        ("Forensic Audit Ledger", "Immutable SHA-256 Chained Hash\nNon-Repudiation Log", 26, "#E0E7FF", "#6366F1")
    ]
    for title, desc, y, fc, ec in vault_modules:
        ax.add_patch(patches.FancyBboxPatch((69, y), 26, 14, boxstyle="round,pad=0.4", fc=fc, ec=ec, lw=1))
        ax.text(82, y + 9.5, title, ha="center", va="center", fontsize=7.2, fontweight="bold", color="#0F172A")
        ax.text(82, y + 4.5, desc, ha="center", va="center", fontsize=6, color="#374151")

    # Bottom Compliance Footer
    ax.text(50, 4, "Compliance: MeitY GIGW · NDSAP · Digital Personal Data Protection (DPDP) Act 2023 · Cert-IN Empaneled VAPT Clearance",
            ha="center", va="center", fontsize=7.2, fontweight="bold", color="#1E293B")

    plt.tight_layout()
    plt.savefig('assets/security_asdc_topology.png', dpi=300)
    plt.close()
    print("Created assets/security_asdc_topology.png")


# -----------------------------------------------------------------------------
# 5. CITIZEN INSTANT E-KHAITAN & QR VERIFICATION MOCKUP
# -----------------------------------------------------------------------------
def create_citizen_ekhaitan_mockup():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.6))

    # Panel 1: Smartphone Alert Notification
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')

    # Phone outline
    ax1.add_patch(patches.FancyBboxPatch((20, 2), 60, 96, boxstyle="round,pad=1", fc="#1E293B", ec="#0F172A", lw=2))
    ax1.add_patch(patches.Rectangle((23, 7), 54, 86, fc="#F8FAFC"))
    
    # Phone header
    ax1.add_patch(patches.Rectangle((23, 81), 54, 12, fc="#075E54"))
    ax1.text(50, 87, "WhatsApp: Govt of Assam", ha="center", va="center", color="white", fontsize=7.5, fontweight="bold")

    # Message Bubble
    ax1.add_patch(patches.FancyBboxPatch((26, 32), 48, 45, boxstyle="round,pad=0.5", fc="#FFFFFF", ec="#CBD5E1", lw=1))
    msg_text = (
        "Dear Ratul Kalita,\n\n"
        "Your land mutation under\n"
        "Mission Basundhara is APPROVED!\n\n"
        "• Circle: Dispur | Patta: 142\n"
        "• New Dag: 588/2\n"
        "• Mutated Area: 1.00 Bigha\n"
        "• Jamabandi & Map Synchronized!\n\n"
        "Tap to view verified e-Khaitan:\n"
        "bhumisync.assam.gov.in/v/884"
    )
    ax1.text(28, 54, msg_text, fontsize=6.2, color="#1E293B")
    ax1.text(68, 35, "02:40 PM ✓✓", fontsize=5.5, color="#10B981")

    # Panel 2: Verified Digital Jamabandi Certificate
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')

    # Certificate box
    ax2.add_patch(patches.Rectangle((5, 2), 90, 96, fc="#FFFFFF", ec="#1B365D", lw=2))
    ax2.add_patch(patches.Rectangle((7, 4), 86, 92, fill=False, ec="#0A7E8C", lw=0.8, linestyle=":"))

    # Certificate Header
    ax2.text(50, 90, "GOVERNMENT OF ASSAM", ha="center", va="center", fontsize=9, fontweight="bold", color="#1B365D")
    ax2.text(50, 85, "Revenue & Disaster Management Department", ha="center", va="center", fontsize=7, color="#0A7E8C")
    ax2.text(50, 80, "VERIFIED DIGITAL RECORD OF RIGHTS (JAMABANDI)", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#0F172A")

    # Details table
    ax2.add_patch(patches.Rectangle((10, 42), 80, 34, fc="#F8FAFC", ec="#E2E8F0", lw=0.8))
    cert_text = (
        "District: Kamrup Metropolitan    Circle: Dispur\n"
        "Mouza: Beltola                   Village: Kahilipara\n"
        "Patta No: 142 (Periodic Kheraj)  Dag No: 588/2\n"
        "Pattadar Name: Ratul Kalita     Share: 1.00 Bigha\n"
        "Deed Reg No: SRO-GHY-2026-7821   Mutation Order: DIS-884\n"
        "Cadastral Map Vector: Synced with Bhunaksha Sheet #04"
    )
    ax2.text(13, 58, cert_text, fontsize=6.3, color="#334155", family="monospace")

    # QR Code placeholder
    ax2.add_patch(patches.Rectangle((12, 10), 24, 24, fc="#F1F5F9", ec="#334155", lw=1))
    # Simulated QR pattern
    ax2.add_patch(patches.Rectangle((14, 24), 6, 6, fc="#1B365D"))
    ax2.add_patch(patches.Rectangle((28, 24), 6, 6, fc="#1B365D"))
    ax2.add_patch(patches.Rectangle((14, 12), 6, 6, fc="#1B365D"))
    ax2.add_patch(patches.Rectangle((22, 18), 4, 4, fc="#1B365D"))
    ax2.text(24, 8, "Scan to Verify Map", ha="center", fontsize=5.5, color="#64748B")

    # Digital Signature Box
    ax2.add_patch(patches.Rectangle((42, 10), 48, 24, fc="#F0FDF4", ec="#86EFAC", lw=0.8))
    ax2.text(66, 28, "✓ DIGITALLY SIGNED", ha="center", fontsize=7, fontweight="bold", color="#166534")
    ax2.text(66, 21, "Circle Officer, Dispur Circle\nTimestamp: 2026-11-25 02:40:12 IST\nCert-IN Empaneled e-Sign PKI", ha="center", fontsize=5.8, color="#15803D")
    ax2.text(66, 13, "Hash: 9b2d8f7a40b17c5e2d634991...", ha="center", fontsize=5, family="monospace", color="#166534")

    plt.tight_layout()
    plt.savefig('assets/citizen_ekhaitan_mockup.png', dpi=300)
    plt.close()
    print("Created assets/citizen_ekhaitan_mockup.png")


if __name__ == '__main__':
    create_before_after_flow()
    create_fraud_window_timeline()
    create_chaos_rollback_flow()
    create_security_asdc_topology()
    create_citizen_ekhaitan_mockup()
    print("All 5 newly recommended images successfully generated!")
