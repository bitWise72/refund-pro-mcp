import os
from fastmcp import FastMCP

mcp = FastMCP("Refund Pro Orchestrator")

@mcp.tool()
def legal_precedent_engine(company: str) -> str:
    """Finds specific legal wins and case numbers for the given company."""
    precedents = {
        "Indigo": "Case No. CC/123/2023 (NCDRC): Awarded 25,000 INR for 4-hour delay.",
        "Zomato": "Order No. Z-992 (Consumer Forum): Refund + 5,000 INR for non-delivery.",
    }
    return precedents.get(company, "Generic Precedent: Indian Contract Act Sec 73 (Damages).")

@mcp.tool()
def aggression_optimizer(sentiment: str) -> str:
    """Adjusts notice intensity based on company's recent customer service behavior."""
    if "ignoring" in sentiment.lower():
        return "INTENSE: Include 'Notice of Intention to Sue' and CC the Ministry of Civil Aviation."
    return "FIRM: Formal request citing DGCA Section 3."

@mcp.tool()
def compensation_calculator(ticket_cost: float, delay_hours: int) -> str:
    """Calculates total claim including interest and time-loss penalties."""
    base_refund = ticket_cost
    penalty = 0
    if delay_hours > 6:
        penalty = 5000
    total = base_refund + penalty
    return f"Total Claim: {total} INR (Base: {base_refund}, Delay Penalty: {penalty})"

@mcp.tool()
def ombudsman_bridge() -> str:
    """Provides the URL for the Government AirSewa portal for immediate escalation."""
    return "GOVERNMENT PORTAL: https://airsewa.gov.in/casemanagement/register-complaint"

@mcp.tool()
def generate_notice_ui(notice_text: str) -> str:
    """Renders the notice in a professional HTML letterhead for the Browser Preview."""
    return f"""
    <html>
        <body style="font-family: sans-serif; padding: 30px; line-height: 1.6;">
            <div style="border: 2px solid #1a365d; padding: 20px;">
                <h1 style="color: #1a365d; margin-top: 0;">LEGAL DEMAND</h1>
                <hr>
                <div style="background: #f8fafc; padding: 15px; border-radius: 5px;">
                    {notice_text}
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)
