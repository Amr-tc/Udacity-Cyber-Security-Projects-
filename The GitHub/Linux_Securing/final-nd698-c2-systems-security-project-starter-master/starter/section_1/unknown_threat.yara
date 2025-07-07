rule darkl0rd_backdoor
{
    meta:
        author = "@amr"
        version = "0.1"

    strings:
        $domain = "darkl0rd.com"

    condition:
        $domain
}
