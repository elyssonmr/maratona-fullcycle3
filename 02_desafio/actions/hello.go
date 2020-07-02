package actions

import (
	"net/http"

	"github.com/gobuffalo/buffalo"
)

func HelloHandler(c buffalo.Context) error {
	c.Set("contentType", "text/plain")
	return c.Render(http.StatusOK, r.String("Hello Full Cycle"))
}
