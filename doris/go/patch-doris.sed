/^version:/d
/- 9010:9010/a\
      - 8070:8070
/- 9050:9050/a\
      - 8050:8050
/BE_ADDR=172\.20\.80\.3:9050/a\
    entrypoint:\
      - bash\
      - -c\
      - |\
        echo "public_host = localhost" >> /opt/apache-doris/be/conf/be.conf\
        exec bash entry_point.sh
