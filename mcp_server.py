from mcp.server.fastmcp import FastMCP
import json
import os
import datetime

mcp = FastMCP("ThreatShield Security Action Server")

@mcp.tool()
def read_network_logs() -> str:
    """Read the current network log feed from the network schema file.
    
    Returns:
        A JSON string containing the list of network traffic events.
    """
    schema_path = os.path.join(os.path.dirname(__file__), "network_schema.json")
    try:
        if not os.path.exists(schema_path):
            return json.dumps({"error": f"Schema file not found at {schema_path}"})
        with open(schema_path, "r") as f:
            return f.read()
    except Exception as e:
        return json.dumps({"error": f"Failed to read logs: {str(e)}"})

@mcp.tool()
def trigger_firewall_block(ip: str) -> str:
    """Block an IP address on the firewall.
    
    Args:
        ip: The target IP address to block.
        
    Returns:
        A status message indicating success or failure.
    """
    blocklog_path = os.path.join(os.path.dirname(__file__), "blocklog.json")
    try:
        blocks = []
        if os.path.exists(blocklog_path):
            try:
                with open(blocklog_path, "r") as f:
                    blocks = json.load(f)
            except json.JSONDecodeError:
                blocks = []
        
        block_event = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "blocked_ip": ip,
            "status": "BLOCKED"
        }
        blocks.append(block_event)
        
        with open(blocklog_path, "w") as f:
            json.dump(blocks, f, indent=2)
            
        return json.dumps({"status": "success", "message": f"IP {ip} successfully blocked on firewall."})
    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)})

@mcp.tool()
def escalate_to_human(alert_level: str) -> str:
    """Escalate a critical security alert to the human Security Operator.
    
    Args:
        alert_level: The security alert level (e.g., HIGH, CRITICAL).
        
    Returns:
        A confirmation message.
    """
    escalation_path = os.path.join(os.path.dirname(__file__), "escalations.json")
    try:
        escalations = []
        if os.path.exists(escalation_path):
            try:
                with open(escalation_path, "r") as f:
                    escalations = json.load(f)
            except json.JSONDecodeError:
                escalations = []
        
        esc_event = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "alert_level": alert_level,
            "status": "ESCALATED"
        }
        escalations.append(esc_event)
        
        with open(escalation_path, "w") as f:
            json.dump(escalations, f, indent=2)
            
        return json.dumps({"status": "success", "message": f"Security alert escalated to human operator with level {alert_level}."})
    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)})

if __name__ == "__main__":
    mcp.run()
